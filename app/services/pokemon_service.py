import requests
from app.database import dbconnect

base_url = "https://pokeapi.co/api/v2/"

#legger data til i databasen
def add_to_db(pokemon_info):
    connection = dbconnect()
    if connection is None:
        return False
    try: 
        cursor = connection.cursor()
        imageurl = pokemon_info['sprites']['front_default']
        query = """INSERT INTO pokemon (id, pmon, height, weight, imageurl) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (
            pokemon_info['id'],
            pokemon_info['name'].lower(),
            pokemon_info['height'] / 10,
            pokemon_info['weight'] / 10,
            imageurl
        ))
        connection.commit()
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            return False
        else: 
            return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#sjekker om pokemon eksisterer i databasen

def pokemon_exists(pokemon_name, pok_id):
    connection = dbconnect()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        query = "SELECT id FROM pokemon WHERE pmon = %s OR id =%s"
        cursor.execute(query, (pokemon_name.lower(), pok_id))
        result = cursor.fetchone()
        return result is not None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#henter pokemon fra databasen

def pokemon_from_db(pokemon_name, pok_id):
    connection = dbconnect()
    if connection is None:
        return None
    try: 
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id, pmon, height, weight, imageurl FROM pokemon WHERE pmon = %s OR id = %s"  
        cursor.execute(query, (pokemon_name.lower(),pok_id))    
        result = cursor.fetchone()
        return result
    finally:
        if connection.is_connected():
            
            cursor.close()
            connection.close()

#henter data fra Api

def get_pokemon_info(name,pok_id):
    if pok_id == None:
        url = f"{base_url}/pokemon/{name}"
    else:
        url = f"{base_url}/pokemon/{pok_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
