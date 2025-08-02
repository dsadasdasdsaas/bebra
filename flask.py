from flask import Flask, request, jsonify

app = Flask(__name__)

valid_keys = {
    "ABC123": None,
    "XYZ789": None
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
