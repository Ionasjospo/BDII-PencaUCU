import bcrypt
from db_connector import DatabaseConnector

# Inicializar el conector de base de datos
db = DatabaseConnector(host="localhost", port=3307, database="PENCA_UCU", user="root", password="pencaUCU")
db.connect()

def save_user(user):
    username = user["Username"]
    document = user["Document"]
    password = user["Password"]
    champion_prediction = user["Champion_Prediction"]
    second_prediction = user["Second_Prediction"]

    # Verificar si el usuario ya existe
    if find_user(username):
        return False  # El usuario ya existe

    # Obtener los IDs de los países
    id_champion = get_country_id(champion_prediction)
    id_sub_champion = get_country_id(second_prediction)
    if id_champion is None or id_sub_champion is None:
        return False  # Uno o ambos países no existen

    query = (
        "INSERT INTO USER (document, username, password, total_points, id_champion, id_sub_champion) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    db.execute_query(query, (document, username, password, 0, id_champion, id_sub_champion))
    return True

def find_user(username):
    query = "SELECT * FROM USER WHERE username = %s"
    results = db.fetch_results(query, (username,))
    if results:
        user = {
            "Username": results[0][2],  
            "Document": results[0][1],  
            "Password": results[0][6],  
            "Champion_Prediction": results[0][8],  
            "Second_Prediction": results[0][9]  
        }
        return user
    return None

def get_countries():
    query = "SELECT id_country, name FROM COUNTRY"
    results = db.fetch_results(query)
    countries = {row[1]: row[0] for row in results}
    return countries


def get_country_id(country_name):
    query = "SELECT id_country FROM COUNTRY WHERE name = %s"
    results = db.fetch_results(query, (country_name,))
    if results:
        return results[0][0]
    return None

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
