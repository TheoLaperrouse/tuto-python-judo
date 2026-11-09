# Python, version judo 🥋

Un petit didacticiel pour découvrir Python sans rien connaître à la programmation.
Fil rouge : aller chercher les champions de judo des Jeux de Paris 2024 dans l'open data publique.

La source des données : le jeu de données « Paris 2024 – Résultats des médaillés pour chaque discipline
Olympique », publié par le ministère des Sports sur data.gouv.fr.
https://www.data.gouv.fr/datasets/672301060dcb9f1a3720e0ec

## Ce qu'il faut

- Python 3 (déjà installé sur la plupart des Linux et des Mac ; tape `python3 --version` dans un terminal pour vérifier).
- Une connexion internet (pour les étapes 2 et 3 et les exercices).
- Aucune bibliothèque à installer : on n'utilise que ce qui est livré avec Python.

## Comment lancer un fichier

Ouvre un terminal dans ce dossier, puis tape par exemple :

```
python3 etape1_les_bases.py
```

Lis le fichier dans un éditeur de texte (VS Code, gedit, Bloc-notes…) en même temps que tu le lances :
tout ce qui suit un `#` est une explication pour toi, Python l'ignore.

## Le parcours

| Fichier | Ce que tu apprends |
|---|---|
| `etape1_les_bases.py` | afficher du texte, les variables, les listes, les boucles, les conditions, les dictionnaires |
| `etape2_recuperer_les_donnees.py` | télécharger des données open data et les regarder |
| `etape3_champions_de_judo.py` | filtrer les données pour ne garder que les champions de judo |
| `exercices/exercice1_les_francais.py` | à toi : les médaillés français |
| `exercices/exercice2_classement_des_pays.py` | à toi : quel pays domine le judo ? |
| `exercices/exercice3_ton_sport.py` | à toi : écrire une fonction pour n'importe quel sport |

Dans les exercices, remplace les `___` par le bon code puis lance le fichier.
Si tu bloques, les corrigés sont dans `exercices/solutions/`… mais essaie d'abord ! 😉

## Si ça plante

C'est normal, ça arrive à tout le monde, tout le temps. Lis la **dernière ligne** du message d'erreur :

- `NameError: name '___' is not defined` → tu as oublié de remplacer un `___`.
- `IndentationError` → les espaces en début de ligne ne sont pas alignés. En Python, le décalage compte !
- `SyntaxError` → il manque souvent un `:`, une parenthèse ou un guillemet.
- `URLError` → pas de connexion internet, ou le site est momentanément indisponible.
