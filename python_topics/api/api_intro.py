# How to connect to an API using python 
import requests
base_url = "https://pokeapi.co/api/v2"

def get_pokemon(name):
    main_url = f"{base_url}/pokemon/{name}"
    response = requests.get(main_url) # sending api requests
    if response.status_code == 200 : # to check if it worked // 200 = "ok" 
        print("Pokemon found in database!")
        pokemon_data = response.json() # converting api info (json) to python dict
    else : 
        print("Could not find given Pokemon on the database!")
        return None
    return pokemon_data
def main() : 
    user_input = input("Enter your favourate pokemon!:").lower()
    pokemon_data = get_pokemon(user_input)
    if pokemon_data:
        print(f"Name = {pokemon_data.get('name').capitalize()}")
        print(f"ID = {pokemon_data.get('id')}")
        print(f"Weight = {pokemon_data.get('weight')}")
        print(f"height = {pokemon_data.get('height')}")

if __name__ == "__main__" : 

    main()


