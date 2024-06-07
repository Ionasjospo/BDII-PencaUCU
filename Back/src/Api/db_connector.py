import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Closed connection")

    def execute_query(self, query, params):
        cursor = self.connection.cursor()
        try:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            self.connection.commit()
            print("Query successful executed")
        except Error as e:
            print(f"Error: {e}")

    def fetch_results(self, query, params):
        cursor = self.connection.cursor()
        try:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return None
