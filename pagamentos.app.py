from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pagamentos")
def pagamentos():
    return jsonify({"status": "Pagamento aprovado"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
