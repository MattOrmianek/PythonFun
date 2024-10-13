from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "password":
            return redirect(url_for("other"))
        else:
            return "Invalid credentials"

@app.route("/other")
def other():
    myvalue = "Hello, World!"
    return render_template("other.html", myvalue=myvalue)

@app.template_filter("reverse")
def reverse_filter(s):
    return s[::-1]

@app.template_filter("repeat")
def repeat_filter(s, n):
    return (s + ' ') * n

@app.template_filter("alternate_case")
def alternate_case_filter(s):
    return ''.join([c.lower() if i % 2 == 0 else c.upper() for i,c in enumerate(s)])

@app.route('/redirect')
def redirect_to_other():
    return redirect(url_for('other'))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)