from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("forms.html")


@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

if __name__ == "__main__":
    app.run(debug=True)
