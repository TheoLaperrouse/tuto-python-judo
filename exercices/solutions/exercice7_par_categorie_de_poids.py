# EXERCICE 7 : les catégories dans l'ordre du poids  (⭐⭐⭐)
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice7_par_categorie_de_poids.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)


def poids_de_la_categorie(epreuve):
    if epreuve == "Mixed Team":
        return 999

    morceaux = epreuve.split(" ")
    poids = morceaux[1]
    nombre = int(poids[1:])

    if poids.startswith("+"):
        return nombre + 1
    return nombre


print(poids_de_la_categorie("Men -60 kg") == 60)
print(poids_de_la_categorie("Men +100 kg") == 101)
print(poids_de_la_categorie("Mixed Team") == 999)
print()

champions = [m for m in medailles if m["discipline"] == "Judo" and m["medal_type"] == "Gold Medal"]

champions_tries = sorted(champions, key=lambda m: (m["gender"], poids_de_la_categorie(m["event"])))

print("🥋 Les champions de judo, du plus léger au plus lourd :")
for champion in champions_tries:
    print(f"  {champion['event']:14} {champion['name']:24} {champion['country']}")
