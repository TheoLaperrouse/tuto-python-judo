# EXERCICE 5 : un programme qui pose des questions  (⭐⭐)
#
# Jusqu'ici, nos programmes affichaient toujours la même chose.
# Avec input(), le programme peut te poser une question et utiliser ta réponse.
#
# Objectif : le programme demande un code de pays (FRA, JPN, BRA...) et affiche
# les médailles de judo de ce pays. Il recommence jusqu'à ce que tu appuies
# sur Entrée sans rien écrire.
#
# Remplace chaque ___ par le bon code, puis lance :
#   python3 exercices/exercice5_question_reponse.py
#
# Essaie avec : FRA, jpn (en minuscules !), KOS, puis USA (aucune médaille en judo).

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

medailles_judo = [m for m in medailles if m["discipline"] == "Judo"]


# input() affiche la question, attend que tu tapes quelque chose puis Entrée,
# et renvoie ce que tu as tapé.
# .strip() enlève les espaces en trop, .upper() met tout en MAJUSCULES
# (comme ça, « fra » devient « FRA »).
def demander_un_pays():
    return input("Code du pays (Entrée pour quitter) : ").strip().upper()


code = demander_un_pays()

# « while » répète tant que la condition est vraie.
# != veut dire « est différent de ». "" est un texte vide.
# Indice : on continue tant que le code n'est pas vide.
while code != ___:
    trouvees = [m for m in medailles_judo if m["country_code"] == ___]

    # Indice : si la liste « trouvees » ne contient aucune médaille...
    if len(trouvees) == ___:
        print(f"  Aucune médaille de judo pour {code}. Matte !")
    else:
        print(f"  {len(trouvees)} médaille(s) de judo pour {code} :")
        for m in trouvees:
            print(f"    {m['medal_type']:13} {m['name']:28} {m['event']}")
    print()

    # Indice : on repose la question, sinon la boucle tournerait à l'infini !
    code = ___

print("Sayonara ! 👋")
