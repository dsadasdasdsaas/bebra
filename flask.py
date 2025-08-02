from flask import Flask, request, jsonify

app = Flask(__name__)

valid_keys = {
    "BKO0C3XZXANH13": None,
    "UWXTVSQPBLL3P0": None,
    "0LPZDC7X1DQN2E": None,
    "80XBBS8QU8AWKE": None,
    "A1LLD0WU3HRJXX": None,
    "VVUAHGA5Z14P6Z": None,
    "AQA0H2Z00K14LH": None,
    "BQCDB91G6VZVPN": None,
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

