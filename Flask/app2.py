from flask import Flask, request, render_template, redirect, url_for, Response
import pandas as pd
from lib.parser import read_excel
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

@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
    if request.method == "GET":
        return render_template("file_upload.html")
    elif request.method == "POST":
        file = request.files["file"]
        if file and file.filename:
            file.save(file.filename)
            if file.filename.endswith(".xls") or file.filename.endswith(".xlsx"):
                df = pd.read_excel(request.files["file"])
                return df.to_html()
            else:
                return "File type not supported"
        else:
            return "No file uploaded"

@app.route("/convert_to_csv", methods=["POST"])
def convert_to_csv():
    file = request.files["file"]
    if file and file.filename:
        df = pd.read_excel(file)
        response = Response(df.to_csv(index=False), content_type="text/csv")
        response.headers["Content-Disposition"] = f"attachment; filename={file.filename.split('.')[0]}.csv"
        return response
    else:
        return "No file uploaded"

@app.route("/other")
def other():
    myvalue = "Hello, World!"
    return render_template("other.html", myvalue=myvalue)


@app.template_filter("reverse")
def reverse_filter(s):
    return s[::-1]


@app.template_filter("repeat")
def repeat_filter(s, n):
    return (s + " ") * n


@app.template_filter("alternate_case")
def alternate_case_filter(s):
    return "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(s)])


@app.route("/redirect")
def redirect_to_other():
    return redirect(url_for("other"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
