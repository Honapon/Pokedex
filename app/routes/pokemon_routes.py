from flask import Blueprint, render_template, request
from app.services.pokemon_service import (get_pokemon_info, add_to_db, pokemon_exists, pokemon_from_db)

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = None
    source = None
    error = None
    
    if request.method == 'POST':
        name = request.form['pokemon_name'].lower()
        
        if not pokemon_exists(name):
            info = get_pokemon_info(name)
            if info:
                add_to_db(info)
                pokemon_data = {
                    "id": info["id"],
                    "name": info["name"],
                    "height": info["height"] / 10,
                    "weight": info["weight"] / 10,
                    "image" : info["sprites"]["front_default"]
                }
                source = 'API'
            else: 
                error = "Could not retrieve Pokémon data from API."
        else: 
            db_data = pokemon_from_db(name)
            if db_data:
                pokemon_data = {
                    "id": db_data["id"],
                    "name": db_data["pmon"],
                    "height": db_data["height"] / 10,
                    "weight": db_data["weight"] / 10,
                    "image" : db_data["imageurl"]
                }
                source = 'database'
            else:
                error = "Pokémon not found in database."
                
    return render_template('display.html', pokemon=pokemon_data, source=source, error=error)
    