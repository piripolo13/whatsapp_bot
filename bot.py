from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Bot Attivo!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Ricevuto:", data)  # Debug

    # Risposta predefinita
    risposta = {"status": "received"}
    
    return jsonify(risposta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

