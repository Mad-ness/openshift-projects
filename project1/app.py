#!/usr/bin/env python

import platform

from flask import Flask
app = Flask(__name__)

@app.route('/ping')
def ping_pong(): return "pong"

@app.route('/health')
def health_check(): return "ok"

@app.route('/whoareyou')
def whoareyou(): return platform.node()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

