# EXERCICE 4 : le judo, sport roi de la France ?  (⭐⭐)
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice4_le_sport_roi.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

compteur = {}
total = 0

for medaille in medailles:
    if medaille["country_code"] == "FRA":
        sport = medaille["discipline"]
        compteur[sport] = compteur.get(sport, 0) + 1
        total += 1

print(f"La France a remporté {total} médailles à Paris 2024.")
print()

classement = sorted(compteur, key=lambda s: compteur[s], reverse=True)

print("Top 5 des sports qui rapportent le plus de médailles à la France :")
for sport in classement[:5]:
    print(f"  {sport:20} {compteur[sport]} médailles")
print()

if classement[0] == "Judo":
    print("Confirmé : le judo est le sport roi de la France ! 🥋")
else:
    print(f"Surprise : c'est {classement[0]} qui est en tête !")
