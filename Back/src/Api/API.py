from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import dbmanager
from datetime import datetime, timedelta
from functools import wraps
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your_secret_key'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')  # Changed to standard header
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = dbmanager.get_countries()
    if countries:
        return jsonify(countries), 200
    else:
        return jsonify({"error": "No countries found"}), 404

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    required_fields = ["Username", "Document", "Password", "Champion_Prediction", "Second_Prediction"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    password = data["Password"]
    hashed_password = dbmanager.hash_password(password)

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

    if not dbmanager.save_user(user):
        return jsonify({"error": "User already exists or invalid country"}), 409

    return jsonify("Success!"), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if "Username" not in data or "Password" not in data:
        return jsonify({"error": "Missing Username or Password"}), 400

    user = dbmanager.find_user(data["Username"])
    if user is None:
        return jsonify({"error": "User not found"}), 404

    if dbmanager.check_password(data["Password"], user["Password"]):
        token = jwt.encode({
            'username': user['Username'],
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token}), 200
    else:
        return jsonify({"error": "Invalid user or password"}), 401

@app.route('/matches', methods=['GET'])
@token_required
def matches(current_user):
    group = request.args.get('group')
    show_predictable = request.args.get('predictable', 'false').lower() == 'true'

    if group:
        matches = dbmanager.matches(group)
    else:
        matches = dbmanager.all_matches()

    if show_predictable:
        now = datetime.now()
        matches = [match for match in matches if match['Date'] > now + timedelta(minutes=30)]

    if current_user == "admin":
        now = datetime.now()
        matches = [match for match in matches if match['Date'] < now]

    else:
        predictions = dbmanager.get_user_predictions(current_user)
        for match in matches:
            match['home_score'] = None
            match['away_score'] = None
            if 'id_match' in match:
                for prediction in predictions:
                    if 'id_match' in prediction and match['id_match'] == prediction['id_match']:
                        match['home_score'] = prediction['home_score']
                        match['away_score'] = prediction['away_score']
                        break

    if matches:
        return jsonify(matches), 200
    else:
        return jsonify({"error": "No matches found"}), 404


@app.route('/predictions', methods=['POST'])
@token_required
def submit_predictions(current_user):
    data = request.get_json()
    predictions = data.get('predictions')

    if not predictions:
        return jsonify({"error": "Invalid input"}), 400

    success = dbmanager.insert_predictions(current_user, predictions)
    if success:
        return jsonify({"message": "Predictions submitted successfully"}), 200
    else:
        return jsonify({"error": "Failed to submit predictions"}), 500

@app.route('/submit_matches', methods=['POST'])
@token_required
def submit_matches(current_user):
    if current_user != "admin":
        return jsonify({"error": "Unauthorized access"}), 403

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

@app.route('/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    user = dbmanager.find_user(current_user)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/profile', methods=['PUT'])
@token_required
def update_profile(current_user):
    data = request.form.to_dict()
    if 'profile_picture' in request.files:
        profile_picture = request.files['profile_picture']
        filename = secure_filename(profile_picture.filename)
        profile_picture.save(os.path.join('Assets/Uploads', filename))
        data['Profile_Picture'] = os.path.join('Assets/Uploads', filename)
    data['Username'] = current_user
    success = dbmanager.update_user(data)
    if success:
        return jsonify({"message": "Profile updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update profile"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
