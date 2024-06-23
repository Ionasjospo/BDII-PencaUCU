from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import dbmanager
import schedule
from datetime import datetime, timedelta
import time
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

@app.route('/points', methods=['GET'])
@token_required
def get_points(current_user):
    user_id = dbmanager.get_user_id(current_user)
    points = dbmanager.get_points(user_id)
    if points:
        return jsonify(points), 200
    else:
        return jsonify({"error": "No points found"}), 404

@app.route('/old_predictions', methods=['GET'])
@token_required
def get_old_predictions(current_user):
    user_id = dbmanager.get_user_id(current_user)
    data = dbmanager.get_user_predictions_and_points(user_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No points found"}), 404


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
    results_admin = request.args.get('results_admin', 'false').lower() == 'true'

    if group:
        matches = dbmanager.matches(group)
    else:
        matches = dbmanager.all_matches()

    if show_predictable:
        now = datetime.now()
        matches = [match for match in matches if match['Date'] > now + timedelta(minutes=30)]

    if (current_user == "admin" and results_admin):
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
    if (results_admin and matches == []):
        return '', 204
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
    
    

@app.route('/ranking', methods=['GET'])
@token_required
def ranking(current_user):
    ranking = dbmanager.get_ranking()
    if ranking:
        filtered_ranking = [user for user in ranking if user['Username'] != 'admin']
        return jsonify({"username": current_user, "ranking": filtered_ranking}), 200
    else:
        return jsonify({"error": "No ranking found"}), 500

@app.route('/country/id', methods=['GET'])
def get_country_by_id():
    country_id = request.args.get('id')

    if not country_id or not country_id.isdigit():
        return jsonify({"error": "Invalid country id"}), 400

    country = dbmanager.get_country_by_id(country_id)
    if country:
        return jsonify(country), 200
    else:
        return jsonify({"error": "Country not found"}), 404

@app.route('/notifications', methods=['GET'])
@token_required
def get_notifications(current_user):
    user_id = dbmanager.get_user_id(current_user)
    if not user_id:
        return jsonify({"error": "User not found"}), 404

    notifications = dbmanager.get_notifications(user_id)
    if notifications:
        return jsonify(notifications), 200
    else:
        return jsonify([]), 200  


def notify_users(stage_name):
    users = dbmanager.get_users()
    for user in users:
        if not dbmanager.has_predictions_for_stage(user[0], stage_name):
            dbmanager.send_notification(user[0], f"No has cargado tus predicciones para la etapa {stage_name}.")

def schedule_notifications():
    # Fechas clave para la Copa América 2024
    schedule.every().day.at("09:00").do(check_and_notify, stage_name="Primera ronda - Grupos").until("2024-06-21")
    schedule.every().day.at("09:00").do(check_and_notify, stage_name="Cuartos de final").until("2024-07-05")
    schedule.every().day.at("09:00").do(check_and_notify, stage_name="Semifinales").until("2024-07-10")
    schedule.every().day.at("09:00").do(check_and_notify, stage_name="Final").until("2024-07-14")

def check_and_notify(stage_name):
    today = datetime.today().date()
    key_dates = {
        "Primera ronda - Grupos": datetime(2024, 6, 20).date(),
        "Cuartos de final": datetime(2024, 7, 4).date(),
        "Semifinales": datetime(2024, 7, 9).date(),
        "Final": datetime(2024, 7, 13).date(),
    }
    if today == key_dates[stage_name]:
        notify_users(stage_name)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
