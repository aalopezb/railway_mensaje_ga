from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/mensaje", methods=["GET"])
def mensaje():
    return jsonify({"mensaje": "Hola, ¿cómo estás?"})

@app.route("/", methods=["GET"])
def home():
    return "Microservicio de mensaje en Railway 3.0."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
