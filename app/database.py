import mysql.connector
from mysql.connector import Error

mydb = {
    'host': '10.100.100.210',
    'user': 'pokedata',
    'password': 'pokekopi',
    'database': 'pokedex'
}

mydbLh = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Korn123',
    'database': 'pokedex'
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
    
    
