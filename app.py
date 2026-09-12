from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "AI API is running!"
    })


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "message is required"}), 400

    return jsonify({
        "reply": f"Mesajını aldım: {message}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
