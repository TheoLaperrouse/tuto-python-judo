# EXERCICE 5 : un programme qui pose des questions  (⭐⭐)
#
# CORRIGÉ. Lance :
#   python3 exercices/solutions/exercice5_question_reponse.py

import json
import urllib.request

URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/paris-2024-results-medals-oly-eng/exports/json"

with urllib.request.urlopen(URL) as reponse:
    medailles = json.load(reponse)

medailles_judo = [m for m in medailles if m["discipline"] == "Judo"]


def demander_un_pays():
    return input("Code du pays (Entrée pour quitter) : ").strip().upper()


code = demander_un_pays()

while code != "":
    trouvees = [m for m in medailles_judo if m["country_code"] == code]

    if len(trouvees) == 0:
        print(f"  Aucune médaille de judo pour {code}. Matte !")
    else:
        print(f"  {len(trouvees)} médaille(s) de judo pour {code} :")
        for m in trouvees:
            print(f"    {m['medal_type']:13} {m['name']:28} {m['event']}")
    print()

    code = demander_un_pays()

print("Sayonara ! 👋")
