import requests

def get_joke():
    j = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    return f"{j['setup']}\n{j['punchline']}"

print(get_joke())
