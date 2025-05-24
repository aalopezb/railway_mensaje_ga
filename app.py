from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/mensaje", methods=["GET"])
def mensaje():
    return jsonify({"mensaje": "Hola, ¿cómo estás?"})

@app.route("/", methods=["GET"])
def home():
    return "Microservicio de mensaje en Railway 7.0."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
