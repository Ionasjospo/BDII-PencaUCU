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

def get_user_id(username):
    query = "SELECT id_student FROM USER WHERE username = %s"
    results = db.fetch_results(query, (username,))
    if results:
        return results[0][0]
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

def all_matches():
    query = """
        SELECT id_match, date_match, home.name AS home_team, away.name AS away_team, home.id_country AS id_home_country, away.id_country AS id_away_country
        FROM FOOTBALL_MATCH
        JOIN COUNTRY home ON FOOTBALL_MATCH.id_home_country = home.id_country
        JOIN COUNTRY away ON FOOTBALL_MATCH.id_away_country = away.id_country
    """
    results = db.fetch_results(query, None)
    matches = []
    for row in results:
        match = {
            "id_match": row[0],
            "Date": row[1],
            "Home team": row[2],
            "Away team": row[3],
            "id_home_country": row[4],
            "id_away_country": row[5]
        }
        matches.append(match)
    return matches


def get_user_predictions(username):
    id_user = get_user_id(username)
    if id_user is None:
        return []

    query = """
        SELECT id_match, score_home_country, score_away_country, id_home_country, id_away_country
        FROM PREDICTION
        WHERE id_user = %s
    """
    results = db.fetch_results(query, (id_user,))
    predictions = []
    for row in results:
        predictions.append({
            "id_match": row[0],
            "home_score": row[1],
            "away_score": row[2],
            "id_home_country": row[3],
            "id_away_country": row[4]
        })
    return predictions

def insert_predictions(username, predictions):
    try:
        id_user = get_user_id(username)
        if id_user is None:
            print(f"User ID not found for username: {username}")
            return False
        
        for prediction in predictions:
            id_match = prediction['id_match']
            home_score = prediction['home_score']
            away_score = prediction['away_score']
            id_home_country = prediction['id_home_country']
            id_away_country = prediction['id_away_country']
            query = """
                INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE score_home_country = %s, score_away_country = %s
            """
            db.execute_query(query, (id_user, id_match, id_home_country, id_away_country, home_score, away_score, home_score, away_score))
        return True
    except Exception as e:
        print(f"Error inserting predictions: {e}")
        return False
    
def insert_matches(matches_updated_data):
    try:
        for match in matches_updated_data:
            if match:                  
                id_match = match['id_match']
                home_score = match['home_score']
                away_score = match['away_score']
                
                query = """
                    UPDATE FOOTBALL_MATCH
                    SET score_home_country = %s,
                    score_away_country = %s
                    WHERE id_match = %s;
                    """
                db.execute_query(query, (home_score, away_score, id_match))
            else:
                print(f"Match data is not completed: {match}")
        return True
    except Exception as e:
        print(f"Error inserting the match results: {e}")
        return False

def update_predictions_points():
    try:
        exact_results_query = """
                    WITH exact_result AS (
                        SELECT P.id_user, P.id_match
                        FROM FOOTBALL_MATCH FM
                        INNER JOIN PREDICTION P ON FM.id_match = P.id_match
                        WHERE FM.score_home_country = P.score_home_country
                        AND FM.score_away_country = P.score_away_country
                    )
                    UPDATE PREDICTION
                    SET points = 4
                    WHERE (id_user, id_match) IN (
                        SELECT id_user, id_match
                        FROM exact_result
                    );
                """
        db.execute_query(exact_results_query, None)

        winners_query = """
                    WITH winner_result AS (
                        SELECT
                            P.id_user,
                            P.id_match
                        FROM FOOTBALL_MATCH FM
                        INNER JOIN PREDICTION P ON FM.id_match = P.id_match
                        WHERE FM.id_winner = CASE
                                                WHEN P.score_home_country > P.score_away_country THEN P.id_home_country
                                                WHEN P.score_home_country < P.score_away_country THEN P.id_away_country
                                            END
                    )
                    UPDATE PREDICTION
                    SET points = 2
                    WHERE (id_user, id_match) IN (
                        SELECT id_user, id_match
                        FROM winner_result
                    );
                """
        db.execute_query(winners_query, None)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def update_user_points():
    try:
        query = """
                WITH Total_points AS (
                    SELECT id_user, SUM(points) as Total_Points
                    FROM PREDICTION
                    WHERE points IS NOT NULL
                    GROUP BY id_user
                )
                UPDATE USER
                SET total_points = (SELECT Total_Points FROM Total_points WHERE Total_points.id_user = USER.id_student)
                WHERE id_student IN (SELECT id_user FROM Total_points);
            """
        db.execute_query(query, None)
        return True
    except Exception as e:
            print(f"Error: {e}")
            return False

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

