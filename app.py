import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "0.1.0")


@app.route("/")
def index():
    return render_template("index.html", version=APP_VERSION)


@app.route("/health")
def health():
    """Used by the Jenkins pipeline / container orchestrator for liveness checks."""
    return jsonify(status="ok", version=APP_VERSION), 200


@app.route("/api/charge", methods=["GET"])
def charge():
    """Trivial API endpoint so there's something real for tests to exercise."""
    return jsonify(message="flash charged", version=APP_VERSION), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
