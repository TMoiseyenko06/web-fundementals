import requests
from digital_cosmos import fetch_planet_data

planets = fetch_planet_data()

def find_heaviest_planet(planets):
    heaviest = ('base',-1,0)
    for planet in planets:
        if planet[1] > heaviest[1]:
            heaviest = planet
    return heaviest

find_heaviest_planet(planets)

name, mass, orbit = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")