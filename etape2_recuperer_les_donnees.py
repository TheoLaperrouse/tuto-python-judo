# ÉTAPE 2 : aller chercher des données sur internet
# Lance ce fichier avec :  python3 etape2_recuperer_les_donnees.py
#
# L'open data, ce sont des données publiques que tout le monde peut utiliser.
# Le ministère des Sports publie sur data.gouv.fr la liste de TOUTES les
# médailles des Jeux Olympiques de Paris 2024. On va la télécharger.


# --- 1. Importer des outils --------------------------------------------------
# Python est livré avec des « modules » : des boîtes à outils toutes prêtes.
# « import » permet de les utiliser.

import json              # pour lire le format JSON (le format des données)
import urllib.request    # pour télécharger une page ou un fichier sur internet


# --- 2. Télécharger les données ----------------------------------------------
# L'adresse du fichier (trouvée sur la page du jeu de données sur data.gouv.fr).
# Par convention, on écrit en MAJUSCULES une valeur qui ne changera jamais.

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

print("Téléchargement des médailles de Paris 2024...")

# « with » ouvre la connexion et la referme proprement à la fin.
# json.load() transforme le texte reçu en données Python :
# ici, une LISTE de DICTIONNAIRES (une fiche par médaille).
with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

print(f"C'est fait : {len(medailles)} médailles récupérées !")
print()


# --- 3. Regarder à quoi ressemble une médaille -------------------------------
# medailles[0] est la première fiche de la liste.
# .items() donne chaque paire « clé, valeur » du dictionnaire.

print("Voici la première fiche :")
premiere = medailles[0]
for cle, valeur in premiere.items():
    print(f"  {cle:16} -> {valeur}")
print()

# Les clés sont en anglais. Les plus utiles pour nous :
#   "discipline"   le sport            (ex : "Judo")
#   "event"        l'épreuve           (ex : "Men -60 kg")
#   "medal_type"   la médaille         ("Gold Medal", "Silver Medal", "Bronze Medal")
#   "name"         le ou la médaillé·e
#   "country"      le pays             (ex : "France")
#   "country_code" le code du pays     (ex : "FRA")


# --- 4. Lister les sports présents -------------------------------------------
# Un « set » (ensemble) ne garde qu'un seul exemplaire de chaque valeur :
# pratique pour enlever les doublons. sorted() trie par ordre alphabétique.

sports = set()
for medaille in medailles:
    sports.add(medaille["discipline"])

print(f"Ces médailles couvrent {len(sports)} sports :")
for sport in sorted(sports):
    print(f"  - {sport}")
print()
print("Le judo est bien là ! Passe à l'étape 3 : python3 etape3_champions_de_judo.py")
