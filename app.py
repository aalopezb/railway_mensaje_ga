from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/mensaje", methods=["GET"])
def mensaje():
    return jsonify({"mensaje": "Hola, ¿cómo estás?"})

@app.route("/", methods=["GET"])
def home():
    return "Microservicio de mensaje en Railway."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
