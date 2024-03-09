import mysql.connector
import os

class MySQLDB:
    def __init__(self, host, user, passsword, database):
        self.host= host
        self.user = user
        self.pw = passsword
        self.da = database
        self.connection = None
    
    def connect(self):
        try:
            if(self.connection== None):
                self.connection = mysql.connector.connect(
                    host = self.host
                    user = self.user,
                    password = self.pw,
                    database = self.db
                )

                os.system("color a2")
                print("wow")
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando {}".format(error))
   
    def disconnect(self):
        try:
            if self.conncection:
                self.connection.close
                self.connection = None
        except mysql.connector.Error as error:
            print ("Erorr")
    def execute_query(self, query, param=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute (query.params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")

db =MySQLDB("Localhost", "root", "", "txp")
print ("conectado")

db.connect()

categorias =db.execute_query("select * from categoria")