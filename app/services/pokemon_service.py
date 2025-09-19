import requests
from app.database import dbconnect

base_url = "https://pokeapi.co/api/v2/"

def add_to_db(pokemon_info):
    connection = dbconnect()
    if connection is None:
        return False
    try: 
        cursor = connection.cursor()
        query = """INSERT INTO pokemon (id, pokémon, height, weight) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (
            pokemon_info['id'],
            pokemon_info['name'].lower(),
            pokemon_info['height'] / 10,
            pokemon_info['weight'] / 10
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

def pokemon_exists(pokemon_name):
    connection = dbconnect()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        query = "SELECT id FROM pokemon WHERE pokémon = %s"
        cursor.execute(query, (pokemon_name.lower(),))
        result = cursor.fetchone()
        return result is not None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def pokemon_from_db(pokemon_name):
    connection = dbconnect()
    if connection is None:
        return None
    try: 
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id, pokémon, height, weight FROM pokemon WHERE pokémon = %s"  
        cursor.execute(query, (pokemon_name.lower(),))    
        result = cursor.fetchone()
        return result
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
