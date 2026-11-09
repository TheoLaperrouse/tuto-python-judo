# EXERCICE 4 : le judo, sport roi de la France ?  (⭐⭐)
#
# On dit souvent que le judo est le sport qui rapporte le plus de médailles
# olympiques à la France. Vérifions avec les données de Paris 2024 !
#
# Objectif : compter les médailles françaises de CHAQUE sport, puis afficher
# le top 5 des sports qui ont rapporté le plus de médailles à la France.
#
# Remplace chaque ___ par le bon code, puis lance :
#   python3 exercices/exercice4_le_sport_roi.py
#
# Résultat attendu : 64 médailles au total, et le judo en tête avec 10 médailles.

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

# Indice : c'est la même idée que l'exercice 2, mais à l'envers.
# On ne garde que la France, et on compte par sport (au lieu de par pays).
compteur = {}
total = 0

for medaille in medailles:
    if medaille["country_code"] == ___:
        sport = medaille[___]
        compteur[sport] = compteur.get(sport, 0) + 1
        total += 1

print(f"La France a remporté {total} médailles à Paris 2024.")
print()

classement = sorted(compteur, key=lambda s: compteur[s], reverse=True)

# Une liste peut se « découper » : liste[:5] donne les 5 premiers éléments.
# Indice : on veut les 5 premiers sports du classement.
print("Top 5 des sports qui rapportent le plus de médailles à la France :")
for sport in ___:
    print(f"  {sport:20} {compteur[sport]} médailles")
print()

# Dernière question : le judo est-il bien premier ?
# classement[0] est le premier élément du classement.
if classement[0] == ___:
    print("Confirmé : le judo est le sport roi de la France ! 🥋")
else:
    print(f"Surprise : c'est {classement[0]} qui est en tête !")
