from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        st = request.form["st"]
        out=""
        for x in st:
            if ord('a') <= ord(x) <= ord('z'):
                out = out + chr(25 - (ord(x) - ord('a')) + ord('a'))
            else:
                out = out + x
        return render_template("index.html", sto=out)
    else:
        return render_template("index.html")

@app.route("/index", methods=["POST", "GET"])
def index2():
    if request.method == "POST":
        dst = request.form["dst"]
        out=""
        for x in dst:
            if ord('a') <= ord(x) <= ord('z'):
                out = out + chr(25 - (ord(x) - ord('a')) + ord('a'))
            else:
                out = out + x
        return render_template("index.html", dsto=out)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)