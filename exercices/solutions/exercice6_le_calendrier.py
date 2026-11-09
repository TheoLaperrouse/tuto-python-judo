# EXERCICE 6 : réparer les dates et faire le calendrier  (⭐⭐⭐)
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice6_le_calendrier.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)


def corriger_date(texte):
    annee, milieu, fin = texte.split("-")
    if fin == "08":
        return f"{annee}-08-{milieu}"
    return texte


print(corriger_date("2024-02-08") == "2024-08-02")
print(corriger_date("2024-07-27") == "2024-07-27")
print()

MOIS = {"07": "juillet", "08": "août"}

champions = [m for m in medailles if m["discipline"] == "Judo" and m["medal_type"] == "Gold Medal"]

print("🗓️  Le calendrier des titres de judo à Paris 2024 :")
for champion in sorted(champions, key=lambda m: corriger_date(m["medal_date"])):
    annee, mois, jour = corriger_date(champion["medal_date"]).split("-")
    date_lisible = f"{int(jour)} {MOIS[mois]}"
    print(f"  {date_lisible:12} {champion['event']:14} {champion['name']}")
