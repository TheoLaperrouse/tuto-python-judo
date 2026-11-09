# ÉTAPE 3 : trouver les champions olympiques de judo
# Lance ce fichier avec :  python3 etape3_champions_de_judo.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

print("Téléchargement des médailles de Paris 2024...")
with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)
print()


# --- 1. Filtrer : ne garder que le judo --------------------------------------
# On part d'une liste vide [ ], on parcourt toutes les médailles,
# et on ajoute (.append) seulement celles dont la discipline est "Judo".
# Attention : == sert à COMPARER (alors que = sert à RANGER).

medailles_judo = []
for medaille in medailles:
    if medaille["discipline"] == "Judo":
        medailles_judo.append(medaille)

print(f"Le judo a distribué {len(medailles_judo)} médailles à Paris 2024.")
print()


# --- 2. Filtrer encore : ne garder que l'or ----------------------------------
# Même principe, mais on écrit cette fois la version courte, très utilisée
# en Python. Elle se lit : « chaque m de medailles_judo, si sa médaille est l'or ».

champions = [m for m in medailles_judo if m["medal_type"] == "Gold Medal"]


# --- 3. Trier et afficher ----------------------------------------------------
# sorted(..., key=...) trie selon le critère qu'on lui donne :
# ici, le nom de l'épreuve. « lambda m: m["event"] » est une mini-fonction
# qui, pour une médaille m, renvoie son épreuve.

print("🥇 Les champions olympiques de judo à Paris 2024 :")
print()
for champion in sorted(champions, key=lambda m: m["event"]):
    print(f"  {champion['event']:14} {champion['name']:24} {champion['country']}")
print()


# --- 4. Un petit compteur ----------------------------------------------------
# Combien de titres pour la France ? On part de 0 et on ajoute 1
# à chaque champion français (+= 1 veut dire « ajoute 1 »).

titres_france = 0
for champion in champions:
    if champion["country_code"] == "FRA":
        titres_france += 1

print(f"La France a remporté {titres_france} titres olympiques en judo à Paris.")
print()
print("Ippon ! Tu sais maintenant télécharger et filtrer des données.")
print("À toi de jouer avec les exercices du dossier « exercices » !")
