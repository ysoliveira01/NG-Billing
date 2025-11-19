from flask import Flask, jsonify
import os

app = Flask(__name__)
DIRECTORY = "/data"

@app.get("/files")
def list_files():
    try:
        files = os.listdir(DIRECTORY)
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # desenvolvimento local
    app.run(host="0.0.0.0", port=5000)
