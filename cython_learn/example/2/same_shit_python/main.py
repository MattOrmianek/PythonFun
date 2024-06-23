""" This is example of a simple cython function complicated with external modules """
import time
import logging
from flask import Flask, request, jsonify
from functools import wraps
from module1 import fibonacci

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class Timethis:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        t0 = time.time()
        result = self.func(*args, **kwargs)
        t1 = time.time()
        logger.info("Time for function is %s seconds", t1 - t0)
        return result

@app.route('/fibonacci', methods=['GET'])
@Timethis
def get_fibonacci():
    try:
        stars = []
        n = int(request.args.get('n'))
        if n <= 0:
            raise ValueError("The number must be a positive integer")

        fib_number = fibonacci(n)
        for _ in range(fib_number):
            stars.append('*')

        return jsonify({"fibonacci": fib_number, "stars": len(stars)}), 200

    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

# for cython - for n = 50 -> 2.49 seconds
# for python - for n = 50 -> 0.60 seconds


# python setup.py build_ext --inplace && python -c "import main; main.main()"