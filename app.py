from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
    return render_template("about.html")