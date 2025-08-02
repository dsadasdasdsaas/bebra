from flask import Flask, request, jsonify

app = Flask(__name__)

valid_keys = {
    "A9F3J7K2": None,
    "B8L5M1Q9": None,
    "X7Z2V4C8": None,
    "M6N9P0S3": None,
    "Q4R8T1W5": None,
    "D3G7H9J0": None,
    "V1X6Z2B4": None,
    "K5L8N3F7": None
}

@app.route("/api/verify", methods=["POST"])
def verify_key():
    data = request.json
    key = data.get("key")
    system_id = data.get("system_id")

    if key not in valid_keys:
        return jsonify({"status": "invalid"}), 400

    if valid_keys[key] is None:
        valid_keys[key] = system_id
        return jsonify({"status": "ok"}), 200
    elif valid_keys[key] == system_id:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "denied"}), 403
        
@app.route("/", methods=["GET"])
def home():
    return "Server is running", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


