import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, host, port, database, user, password):
        if not hasattr(self, 'initialized'):
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.password = password
            self.connection = None
            self.initialized = True

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
            self.connection.rollback()
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
    
    def fetch_one(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            
