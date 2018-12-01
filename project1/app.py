#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/ping')
def ping_pong(): return "pong"

@app.route('/health')
def health_check(): return "ok"

if __name__ == "__main__":
    app.run(debug=True, port=8080)

