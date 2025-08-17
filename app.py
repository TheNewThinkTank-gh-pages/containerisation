# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
        message="Hello from a containerized Python app!",
        environment=os.getenv("APP_ENV", "development")
    )

if __name__ == "__main__":
    # Best practice: don’t hardcode host/port, use env vars
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

