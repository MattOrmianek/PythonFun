from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello_world():
    myvalue = "Hello, World!"
    mylist = [1, 2, 3, 4, 5] 
    return render_template("index.html", myvalue=myvalue, mylist=mylist)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)