import mysql.connector
import sys

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Some erroe occured Could not connect to database")
            sys.exit(0)
            
        else:
            print("Connected to database")
            