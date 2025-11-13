# Lab 05 – API Joke avec Python & Docker

Application Python 3 utilisant la bibliothèque `requests` pour interroger une API publique et afficher une blague.

---

## Fonctionnalités

- Récupère une blague aléatoire depuis l'API [JokesAPI]
- Gère les erreurs réseau
- Compatible avec ou sans Docker

---

## Prérequis

- Python version 3.8 ou +
- `pip` (gestionnaire de paquets Python)
- Docker (Optionnel)

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/AdrienMeys/ue19-lab-05.git
   cd ue19-lab-05
   ```

2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement de l'application app.py

1. Sans docker : 
   ```bash
   python app.py
   ```
2. Avec docker : 
   ```bash
   docker build -t joke-app .
   docker run joke-app
   ```
