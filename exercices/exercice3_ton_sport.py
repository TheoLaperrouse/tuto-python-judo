# EXERCICE 3 : une fonction pour n'importe quel sport
#
# Jusqu'ici, on recopiait le même code à chaque fois. Une FONCTION permet
# d'écrire un morceau de code une seule fois, de lui donner un nom, et de le
# réutiliser autant qu'on veut avec des valeurs différentes.
#
# Objectif : écrire la fonction afficher_champions(sport) qui affiche les
# champions olympiques (médaille d'or) du sport demandé.
#
# Remplace chaque ___ par le bon code, puis lance :
#   python3 exercices/exercice3_ton_sport.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)


# « def » crée une fonction. Ce qu'il y a entre parenthèses (sport) est un
# « paramètre » : une variable qui prendra la valeur donnée à chaque appel.
def afficher_champions(sport):
    print(f"🥇 Champions olympiques de {sport} :")
    for medaille in medailles:
        # Indice : la discipline doit être égale au paramètre de la fonction,
        # et la médaille doit être "Gold Medal".
        if medaille["discipline"] == ___ and medaille["medal_type"] == ___:
            print(f"  {medaille['event']:32} {medaille['name']:28} {medaille['country']}")
    print()


# On « appelle » la fonction en lui donnant un sport.
afficher_champions("Judo")

# Indice : appelle la fonction une deuxième fois, pour l'escrime ("Fencing").
___

# À toi de choisir ! Lance d'abord l'étape 2 pour voir la liste des sports
# disponibles (attention, les noms sont en anglais), puis appelle la fonction
# avec ton sport préféré : "Swimming" (natation), "Cycling Track" (cyclisme sur
# piste), "Rugby Sevens", "Taekwondo", "Wrestling" (lutte)...
