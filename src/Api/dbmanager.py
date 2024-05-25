import bcrypt
from db_connector import DatabaseConnector

# Inicializar el conector de base de datos
db = DatabaseConnector(host="localhost", port=3307, database="PENCA_UCU", user="root", password="pencaUCU")
db.connect()

def save_user(user):
    document = user["Document"]
    username = user["Username"]
    name = user["Name"]
    surname = user["Surname"]
    email = user["Email"]
    password = user["Password"]
    total_points = 0
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
        "INSERT INTO USER (document, username, name, surname, email, password, total_points, id_champion, id_sub_champion) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    db.execute_query(query, (document, username, name, surname, email, password, total_points, id_champion, id_sub_champion))
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
    results = db.fetch_results(query, params=None)
    countries = {row[1]: row[0] for row in results}
    return countries

def matches(group):
    # In the first stages, the same countries group plays against each other
    group2 = group
    query = (
        "SELECT date_match, home.name, away.name "
        "FROM FOOTBALL_MATCH "
        "JOIN COUNTRY home ON FOOTBALL_MATCH.id_home_country = home.id_country "
        "JOIN COUNTRY away ON FOOTBALL_MATCH.id_away_country = away.id_country "
        "WHERE home.cup_group = %s AND away.cup_group = %s"
    )
    results = db.fetch_results(query, (group,group2))
    matches = []
    for row in results:
        match = {
            "Date": row[0],
            "Home team": row[1],
            "Away team": row[2]
        }
        matches.append(match)
    return matches


def get_country_id(country_name):
    query = "SELECT id_country FROM COUNTRY WHERE name = %s"
    results = db.fetch_results(query, (country_name,))
    if results:
        return results[0][0]
    return None

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

