import mysql.connector
from mysql.connector import Error



mydbLh = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': ''
}


# Funksjon for å opprette en tilkobling til databasen
def dbconnect():
    try:
        connection = mysql.connector.connect(**mydb)
        #connection = mysql.connector.connect(**mydbLh)
        return connection
        
        
    except Error as e:
        print(f"Error connecting to mariadb: {e}")
        return None
    
    
