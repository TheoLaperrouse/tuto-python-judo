# EXERCICE 7 : les catégories dans l'ordre du poids  (⭐⭐⭐)
#
# À l'étape 3, les champions étaient triés par ordre alphabétique :
# "Men +100 kg" arrivait AVANT "Men -60 kg", et "-100" avant "-60".
# Normal : pour l'ordinateur, ce sont des textes, pas des poids !
#
# Objectif : écrire une fonction qui extrait le poids d'une catégorie,
# pour trier les champions du plus léger au plus lourd.
#
# Remplace chaque ___ par le bon code, puis lance :
#   python3 exercices/exercice7_par_categorie_de_poids.py
#
# Résultat attendu : les hommes de -60 kg à +100 kg, puis les femmes
# de -48 kg à +78 kg, et l'équipe mixte à la fin.

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)


# Exemples de ce que la fonction doit renvoyer :
#   "Men -60 kg"    ->  60
#   "Women -78 kg"  ->  78
#   "Men +100 kg"   ->  101   (plus lourd que -100 kg, donc un peu plus que 100)
#   "Mixed Team"    ->  999   (pas de poids : on le met tout à la fin)
def poids_de_la_categorie(epreuve):
    if epreuve == "Mixed Team":
        return 999

    # "Men -60 kg".split(" ")  donne  ["Men", "-60", "kg"]
    # Indice : le poids est le 2e morceau... et on compte à partir de 0 !
    morceaux = epreuve.split(" ")
    poids = morceaux[___]

    # poids[1:] enlève le premier caractère : "-60" devient "60".
    # int() transforme le texte "60" en vrai nombre 60.
    nombre = int(poids[1:])

    # .startswith("+") vérifie si un texte commence par « + ».
    # Indice : pour une catégorie « + », on ajoute 1 au nombre.
    if poids.startswith(___):
        return nombre + ___
    return nombre


# Petits tests : si la fonction est juste, tout affiche True.
print(poids_de_la_categorie("Men -60 kg") == 60)
print(poids_de_la_categorie("Men +100 kg") == 101)
print(poids_de_la_categorie("Mixed Team") == 999)
print()

champions = [m for m in medailles if m["discipline"] == "Judo" and m["medal_type"] == "Gold Medal"]

# On trie selon DEUX critères, donnés entre parenthèses : d'abord le genre
# ("M" pour les hommes avant "W" pour les femmes), puis le poids.
champions_tries = sorted(champions, key=lambda m: (m["gender"], poids_de_la_categorie(m["event"])))

print("🥋 Les champions de judo, du plus léger au plus lourd :")
for champion in champions_tries:
    print(f"  {champion['event']:14} {champion['name']:24} {champion['country']}")
