"""Minimal flask application."""
from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"Hello": "World", "HostName": socket.gethostname()})
