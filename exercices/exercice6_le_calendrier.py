# EXERCICE 6 : réparer les dates et faire le calendrier  (⭐⭐⭐)
#
# Les données réelles ne sont jamais parfaites ! Regarde la colonne
# "medal_date" : Teddy Riner aurait gagné le « 2024-02-08 »... le 8 février ?
# Non : les épreuves ont eu lieu du 27 juillet au 11 août 2024.
#
# Le problème : pour les jours d'août, le jour et le mois sont inversés.
#   - juillet : "2024-07-27" est correct  (année-mois-jour)
#   - août    : "2024-02-08" veut dire le 2 août, il faudrait "2024-08-02"
# Repère : quand le texte se termine par "08", c'est une date d'août à l'envers.
#
# Objectif : écrire la fonction corriger_date(), puis afficher le calendrier
# des titres olympiques de judo dans l'ordre chronologique.
#
# Remplace chaque ___ par le bon code, puis lance :
#   python3 exercices/exercice6_le_calendrier.py
#
# Résultat attendu : ça commence le 27 juillet (-60 kg et -48 kg)
# et ça finit le 3 août avec le titre de la France par équipes.

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)


# .split("-") découpe un texte à chaque tiret :
#   "2024-02-08".split("-")  donne  ["2024", "02", "08"]
# On peut ranger les 3 morceaux dans 3 variables d'un coup.
def corriger_date(texte):
    annee, milieu, fin = texte.split(___)
    # Indice : si la fin est "08", c'est une date d'août à l'envers.
    if fin == ___:
        # Indice : on remet dans l'ordre année-mois-jour ; le mois est 08,
        # et le jour, c'est le morceau du milieu.
        return f"{annee}-08-{___}"
    return texte


# Petit test : si la fonction est juste, ces deux lignes affichent True.
print(corriger_date("2024-02-08") == "2024-08-02")
print(corriger_date("2024-07-27") == "2024-07-27")
print()

MOIS = {"07": "juillet", "08": "août"}

champions = [m for m in medailles if m["discipline"] == "Judo" and m["medal_type"] == "Gold Medal"]

# Une fois corrigées, les dates au format année-mois-jour se trient
# toutes seules dans le bon ordre. C'est pour ça que ce format est si utilisé !
print("🗓️  Le calendrier des titres de judo à Paris 2024 :")
for champion in sorted(champions, key=lambda m: corriger_date(m["medal_date"])):
    annee, mois, jour = corriger_date(champion["medal_date"]).split("-")
    date_lisible = f"{int(jour)} {MOIS[mois]}"
    print(f"  {date_lisible:12} {champion['event']:14} {champion['name']}")
