from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def receive_json():
    # Recibir el JSON enviado por POST
    data = request.json

    # Validar que los campos necesarios estén presentes
    required_fields = ["Username", "Document", "Password", "Champion_Prediction", "Second_Prediction"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Hashear la contraseña
    password = data["Password"]
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Puedes procesar o imprimir el JSON recibido aquí
    print("Received JSON:", data)

    # Responder con código 200 y un mensaje JSON
    return jsonify("OK"), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
