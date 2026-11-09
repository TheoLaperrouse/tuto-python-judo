# EXERCICE 2 : quel pays domine le judo ?
#
# Objectif : compter les médailles de judo (toutes couleurs) de chaque pays,
# puis afficher le classement, du pays le plus médaillé au moins médaillé.
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice2_classement_des_pays.py
#
# Résultat attendu : la France en tête avec 10 médailles, devant le Japon (8).

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

# Un dictionnaire vide qui va servir de tableau des scores :
# la clé sera le pays, la valeur son nombre de médailles.
# Par exemple, à la fin : {"France": 10, "Japan": 10, ...}
compteur = {}

for medaille in medailles:
    if medaille["discipline"] == "Judo":
        pays = medaille["country"]
        # .get(pays, 0) renvoie le nombre déjà compté pour ce pays,
        # ou 0 si on ne l'a encore jamais rencontré.
        # Indice : on veut ajouter UNE médaille de plus.
        compteur[pays] = compteur.get(pays, 0) + 1

# On trie les pays selon leur nombre de médailles.
# reverse=True veut dire « du plus grand au plus petit ».
# Indice : le critère de tri est le nombre de médailles du pays p,
# c'est-à-dire la valeur rangée dans le compteur pour la clé p.
classement = sorted(compteur, key=lambda p: compteur[p], reverse=True)

print("Classement des pays en judo à Paris 2024 :")
rang = 1
for pays in classement:
    print(f"  {rang:2}. {pays:22} {compteur[pays]} médaille(s)")
    rang += 1
