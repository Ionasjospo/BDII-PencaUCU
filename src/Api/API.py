from flask import Flask, request, jsonify
import dbmanager

app = Flask(__name__)

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = dbmanager.get_countries()
    return jsonify(countries), 200

@app.route('/register', methods=['POST'])
def register():
    # Recibir el JSON enviado por POST
    data = request.json

    # Validar que los campos necesarios estén presentes
    required_fields = ["Username", "Document", "Password", "Champion_Prediction", "Second_Prediction"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Hashear la contraseña
    password = data["Password"]
    hashed_password = dbmanager.hash_password(password)

    # Crear el usuario
    user = {
        "Document": data["Document"],
        "Username": data["Username"],
        "Name": data["Name"],
        "Surname": data["Surname"],
        "Email": data["Email"],
        "Password": hashed_password,  
        "Champion_Prediction": data["Champion_Prediction"],
        "Second_Prediction": data["Second_Prediction"]
    }

    # Guardar el usuario en la base de datos
    if not dbmanager.save_user(user):
        return jsonify({"error": "User already exists or invalid country"}), 409

    print("Received JSON:", user)

    # Responder con código 200 y un mensaje JSON
    return jsonify("Success!"), 200

@app.route('/login', methods=['POST'])
def login():
    # Recibir el JSON enviado por POST
    data = request.json

    # Validar que los campos necesarios estén presentes
    if "Username" not in data or "Password" not in data:
        return jsonify({"error": "Missing Username or Password"}), 400

    # Buscar el usuario en la base de datos
    user = dbmanager.find_user(data["Username"])
    if user is None:
        return jsonify({"error": "User not found"}), 404

    print("User found", user["Password"])
    # Verificar la contraseña
    if dbmanager.check_password(data["Password"], user["Password"]):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid user or password"}), 401

@app.route('/football_match', methods=['GET'])
def get_matchs(group):
    matchs = dbmanager.get_matchs()
    return jsonify(matchs), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
