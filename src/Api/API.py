from flask import Flask, request, jsonify
import dbmanager
from datetime import datetime, timedelta

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

@app.route('/matches', methods=['GET'])
def matches():
    group = request.args.get('group')
    show_predictable = request.args.get('predictable', False)
    username = request.args.get('username')
    
    if group:
        matches = dbmanager.matches(group)
    else:
        matches = dbmanager.all_matches()
    
    if show_predictable:
        now = datetime.now()
        filtered_matches = []
        for match in matches:
            if isinstance(match['Date'], str):
                match_datetime = datetime.strptime(match['Date'], "%a, %d %b %Y %H:%M:%S")
            else:
                match_datetime = match['Date']
            if match_datetime > now + timedelta(minutes=30):
                filtered_matches.append(match)
        matches = filtered_matches
    
    if username:
        if username == "admin":
            # Admin doesnt have preditctions, ver cargar mas de un partido 
            for match in matches: 
                if isinstance(match['Date'], str):
                    match_datetime = datetime.strptime(match['Date'], "%a, %d %b %Y %H:%M:%S")
                else:
                    match_datetime = match['Date']
                # If the match already happened    
                if match_datetime < now:
                    filtered_matches.append(match)
            matches = filtered_matches      
        else:
            predictions = dbmanager.get_user_predictions(username)
            for match in matches:
                match['home_score'] = None
                match['away_score'] = None
                for prediction in predictions:
                    if match['id_match'] == prediction['id_match']:
                        match['home_score'] = prediction['home_score']
                        match['away_score'] = prediction['away_score']
                        break

    if matches:
        return jsonify(matches), 200
    else:
        return jsonify({"error": "No matches found"}), 404

    
@app.route('/predictions', methods=['POST'])
def submit_predictions():
    data = request.get_json()
    username = data.get('username')
    predictions = data.get('predictions')

    if not username or not predictions:
        return jsonify({"error": "Invalid input"}), 400

    success = dbmanager.insert_predictions(username, predictions)
    if success:
        return jsonify({"message": "Predictions submitted successfully"}), 200
    else:
        return jsonify({"error": "Failed to submit predictions"}), 500
    
@app.route('/submit_matches', methods=['POST'])
def submit_matches():
    data = request.get_json()
    matches_updated = data['matches_updated']

    if not matches_updated:
        return jsonify({"error": "Invalid input"}), 400

    success = dbmanager.insert_matches(matches_updated)
    if success:
        dbmanager.update_predictions_points()
        dbmanager.update_user_points()
        return jsonify({"message": "Predictions submitted successfully"}), 200
    else:
        return jsonify({"error": "Failed to submit predictions"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
