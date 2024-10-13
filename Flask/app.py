from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "<p>Hello, Mateusz!</p>"

@app.route("/hello/<name>")
def hello_name(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/add/<int:a>/<int:b>") # specified type of variable, default type is string
def add(a, b):
    return f"<p>Sum of {a} and {b} is {a + b}</p>"

@app.route("/add2")
def add2():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return "<p>Error: a or b is not provided</p>", 400
    return f"<p>Sum of {a} and {b} is {a + b}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)