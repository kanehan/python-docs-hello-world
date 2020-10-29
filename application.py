#!C:\Users\omi\AppData\Local\Programs\Python\Python39python.exe
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "hhhello world!"

if __name__ == "__main__":
    app.run(debug=True)