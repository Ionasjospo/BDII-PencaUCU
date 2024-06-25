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

    if find_user(username):
        return False  

    id_champion = get_country_id(champion_prediction)
    id_sub_champion = get_country_id(second_prediction)
    if id_champion is None or id_sub_champion is None:
        return False  

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
            "Name": results[0][3],
            "Surname": results[0][4], 
            "Document": results[0][1],  
            "Password": results[0][6],  
            "Champion_Prediction": results[0][8],  
            "Second_Prediction": results[0][9],
            "Email": results[0][5],
            "Total_Points": results[0][7],
            "Profile_Picture": results[0][10]
        }
        return user
    return None

def get_user_id(username):
    query = "SELECT id_student FROM USER WHERE username = %s"
    results = db.fetch_results(query, (username,))
    if results:
        return results[0][0]
    return None

def get_points(id_user):
    query = "SELECT total_points FROM USER WHERE id_student = %s"
    results = db.fetch_results(query, (id_user,))
    if results:
        return results[0][0]
    return None


def update_user(update_data):
    try:
        query = """
        UPDATE USER
        SET
            name = %s,
            surname = %s,
            email = %s,
            profile_picture = %s
        WHERE username = %s
        """
    
        db.execute_query(query, (
            update_data['first_name'],
            update_data['last_name'],
            update_data['email'],
            update_data['Profile_Picture'],
            update_data['username']
        ))
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        return False

    
def get_users():
    query = "SELECT id_student, username, email FROM USER"
    return db.fetch_results(query, None)

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


def get_user_predictions_and_points(id_user):
    if id_user is None:
        return []

    query = """
        SELECT p.id_match, home_country.name, score_home_country, away_country.name, score_away_country, points FROM PREDICTION p
            JOIN COUNTRY home_country ON p.id_home_country = home_country.id_country
            JOIN COUNTRY away_country ON p.id_away_country = away_country.id_country
        WHERE id_user = %s;
    """
    results = db.fetch_results(query, (id_user,))
    predictions = []
    for row in results:
        predictions.append({
            "id_match": row[0],
            "home_country": row[1],
            "home_score": row[2],
            "away_country": row[3],
            "away_score": row[4],
            "points": row[5]
        })
    
    return predictions

def get_match_results(match_id):
    query = """
        SELECT score_home_country, score_away_country
        FROM FOOTBALL_MATCH
        WHERE id_match = %s
    """
    results = db.fetch_results(query, (match_id,))
    if results:
        return {
            "home_score": results[0][0],
            "away_score": results[0][1]
        }
    return None


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

def update_winner_matches():
    try:
        query = """
            UPDATE FOOTBALL_MATCH
            SET id_winner = CASE
                WHEN score_home_country > score_away_country THEN id_home_country
                WHEN score_home_country < score_away_country THEN id_away_country
                WHEN score_home_country = score_away_country THEN 17
            END
            WHERE id_winner IS NULL
            AND score_home_country IS NOT NULL
            AND score_away_country IS NOT NULL;
        """
        db.execute_query(query, None)
        return True
    except Exception as e:
        print(f"Error updating winner matches: {e}")
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
                                                ELSE 17
                                            END
                            AND !(FM.score_home_country = P.score_home_country AND FM.score_away_country = P.score_away_country)
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

def get_ranking():
    query = "SELECT username, total_points, id_champion, id_sub_champion FROM USER ORDER BY total_points DESC"
    results = db.fetch_results(query, None)
    ranking = []
    print(results)
    for row in results:
        rank= {
            "Username": row[0],
            "Total Points": row[1],
            "Champion": row[2],
            "Sub Champion": row[3]
        }
        ranking.append(rank)
    return ranking

def get_country_by_id(country_id):
    query = "SELECT name FROM COUNTRY WHERE id_country = %s"
    results = db.fetch_results(query, (country_id,))
    if results:
        return results[0][0]
    return None

def has_predictions_for_stage(user_id, stage_name):
    query = """
    SELECT COUNT(*)
    FROM PREDICTION
    JOIN FOOTBALL_MATCH ON PREDICTION.id_match = FOOTBALL_MATCH.id_match
    JOIN STAGE ON FOOTBALL_MATCH.id_stage = STAGE.id_stage
    WHERE PREDICTION.id_user = %s AND STAGE.name = %s
    """
    result = db.fetch_results(query, (user_id, stage_name))
    return result[0][0] > 0

def send_notification(user_id, message):
    query = "INSERT INTO NOTIFICATION (id_user, message) VALUES (%s, %s)"
    db.execute_query(query, (user_id, message))

def get_notifications(user_id):
    query = "SELECT id_notification, message FROM NOTIFICATION WHERE id_user = %s"
    results = db.fetch_results(query, (user_id,))
    notifications = [{"id_notification": row[0], "message": row[1]} for row in results]
    return notifications

def get_match_by_id(user, match_id):
    id_user = get_user_id(user)
    query = """
        SELECT id_match, date_match, home.name AS home_team, away.name AS away_team
        FROM FOOTBALL_MATCH
        INNER JOIN COUNTRY home ON FOOTBALL_MATCH.id_home_country = home.id_country
        INNER JOIN COUNTRY away ON FOOTBALL_MATCH.id_away_country = away.id_country
        WHERE id_match = %s
    """
    result = db.fetch_results(query, (match_id,))
    match = []
    for row in result:
        match = {
            "id_match": row[0],
            "Date": row[1],
            "Home team": row[2],
            "Away team": row[3]
        }
        return match
    return None

def get_stats(user,match_id):
    user_id = get_user_id(user)
    query = """
                SELECT
                ROUND((SUM(CASE WHEN score_home_country > score_away_country THEN 1 ELSE 0 END) * 100.0 / COUNT(*)),0) as home_win,
                ROUND((SUM(CASE WHEN score_away_country > score_home_country THEN 1 ELSE 0 END) * 100.0 / COUNT(*)),0) as away_win,
                ROUND((SUM(CASE WHEN score_home_country = score_away_country THEN 1 ELSE 0 END) * 100.0 / COUNT(*)),0) as tie
                FROM
                PREDICTION
                WHERE
                id_match = %s
                AND id_user != %s
            """
    result = db.fetch_results(query, (match_id,user_id))
    stats = []
    for row in result:
        stat = {
            "Home_Win": row[0],
            "Away_Win": row[1],
            "Tie": row[2]
        }
        stats.append(stat)
    if stats:
        return stats 
    return None
        






