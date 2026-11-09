# EXERCICE 1 : les médaillés français en judo
#
# Objectif : afficher TOUS les médaillés français du judo à Paris 2024
# (or, argent ET bronze), avec leur médaille écrite en français.
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice1_les_francais.py
#
# Résultat attendu (dans le désordre) : 10 médailles, dont Teddy RINER en or.

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

# Un dictionnaire qui sert de « traducteur » : on lui donne la clé anglaise,
# il rend le texte français. Exemple : en_francais["Gold Medal"] vaut "🥇 or".
en_francais = {
    "Gold Medal": "🥇 or",
    "Silver Medal": "🥈 argent",
    "Bronze Medal": "🥉 bronze",
}

print("Les médailles françaises en judo :")
nombre = 0

for medaille in medailles:
    # Indice : il faut DEUX conditions à la fois, reliées par « and ».
    # Le sport doit être "Judo" ET le code du pays doit être "FRA".
    if medaille["discipline"] == "Judo" and medaille["country_code"] == "FRA":
        # Indice : utilise le dictionnaire en_francais avec la médaille de la fiche.
        traduction = en_francais[medaille["medal_type"]]
        print(f"  {traduction:10} {medaille['name']:28} {medaille['event']}")
        nombre += 1

print(f"Total : {nombre} médailles.")
