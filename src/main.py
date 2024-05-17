from db_connector import DatabaseConnector


class Main:
    def __init__(self):
        self.db_connector = None

    def start(self):
        host = 'localhost'
        port = 3307
        database = 'PENCA_UCU'
        user = 'root'
        password = 'pencaUCU'

        self.db_connector = DatabaseConnector(host, port, database, user, password)
        self.db_connector.connect()
        
        # Aquí puedes realizar tus operaciones con la base de datos
        # Ejemplo: Crear una tabla
        # create_table_query = """
        # CREATE TABLE IF NOT EXISTS students (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     name VARCHAR(255) NOT NULL,
        #     age INT NOT NULL
        # );
        # """
        # self.db_connector.execute_query(create_table_query)

        # # Ejemplo: Insertar datos en la tabla
        # insert_data_query = """
        # INSERT INTO students (name, age) VALUES
        # ('Alice', 23),
        # ('Bob', 22);
        # """
        # self.db_connector.execute_query(insert_data_query)

        # Ejemplo: Recuperar datos de la tabla
        select_query = "SELECT * FROM STUDENT;"
        results = self.db_connector.fetch_results(select_query)
        for row in results:
            print(row)

        # Cierra la conexión
        self.db_connector.close()

if __name__ == "__main__":
    main = Main()
    main.start()
