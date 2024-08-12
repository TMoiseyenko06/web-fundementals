import requests


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()["bodies"]
    planet_info = []
    for planet in planets:
        if planet["isPlanet"]:
            name = planet["name"]
            mass = mass["massValue"] ** mass["massExponent"]
            orbit_period = planet["sideralOrbit"]
            planet_info.append((name, mass, orbit_period))
            if __name__ == "__main__":
                print(
                    f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days"
                )
    return planet_info


fetch_planet_data()
