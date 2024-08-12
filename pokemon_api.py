import requests
import json

# Task 2:
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data = response.text
python_data = json.loads(json_data)
print(python_data["name"], python_data["types"])


# Task 3:
def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    return json.loads(response.text)


def calculate_average_weight(pokemon_list):
    for pokemon in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        data = json.loads(response.text)
        print(data["name"], data["abilities"], data["weight"])


pokemon_names = ["pikachu", "bulbasaur", "charmander"]

fetch_pokemon_data('pikachu')
calculate_average_weight(pokemon_names)
