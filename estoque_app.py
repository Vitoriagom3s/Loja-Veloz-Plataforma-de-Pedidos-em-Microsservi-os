from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/estoque")
def estoque():
    return jsonify({"produto": "Tênis", "quantidade": 10})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
