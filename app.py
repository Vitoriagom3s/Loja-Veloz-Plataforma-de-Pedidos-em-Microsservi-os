from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/pedidos")
def pedidos():
    return jsonify([
        {"id": 1, "produto": "Tênis", "status": "Criado"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
