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
                print("Conectado a la base de datos")
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Consulta ejecutada con éxito")
        except Error as e:
            print(f"Error: {e}")

    def fetch_results(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return None
