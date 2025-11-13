import requests
import sys

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        return f"{joke['setup']}\n{joke['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"Erreur : {e}"

if __name__ == "__main__":
    print("Voici une blague :")
    print(get_joke())
