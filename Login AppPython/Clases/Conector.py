import mysql.connector
class Conector:
    def __init__(self):
        self.host = "localhost" 
        self.user = "root"
        self.password = ""
        self.database = "Pro3_Python"   
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def close(self):
        self.cursor.close()
        self.connection.close()

    # Ejecutar consultas tipo SELECT
    def select(self, sql, values=None):
        try:
            self.cursor = self.conectar()
            self.cursor.execute(sql, values or ())
            results = self.cursor.fetchall()
            self.close()
            return results
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    # Ejecutar consultas tipo INSERT, UPDATE, DELETE
    def execute_query(self, sql, values=None):
        try:
            self.cursor = self.conectar()
            self.cursor.execute(sql, values or ())
            self.connection.commit()
            self.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False


