"""This is example of a simple cython function complicated with external modules"""

from flask import Flask, request, jsonify
from module1 import fibonacci

app = Flask(__name__)


@app.route("/fibonacci", methods=["GET"])
def get_fibonacci():
    try:
        stars = []
        n = int(request.args.get("n"))
        if n <= 0:
            raise ValueError
        fib_number = fibonacci(n)
        for _ in range(fib_number):
            stars.append("*")
        return jsonify({"fibonacci": fib_number, "stars": len(stars)}), 200

    except (TypeError, ValueError):
        return jsonify(
            {"error": "Please provide a valid positive integer for 'n'"}
        ), 400


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
