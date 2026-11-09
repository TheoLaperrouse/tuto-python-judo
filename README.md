# Python, version judo 🥋

Un petit didacticiel pour découvrir Python sans rien connaître à la programmation.
Fil rouge : aller chercher les champions de judo des Jeux de Paris 2024 dans l'open data publique.

La source des données : le jeu de données « Paris 2024 – Résultats des médaillés pour chaque discipline
Olympique », publié par le ministère des Sports sur data.gouv.fr.
https://www.data.gouv.fr/datasets/672301060dcb9f1a3720e0ec

## 1. Installer Python sur un Mac

Python n'est pas installé d'office sur les Mac récents. Voici comment l'ajouter :

1. **Ouvre le Terminal** : appuie sur `Cmd ⌘ + Espace`, tape « Terminal », puis Entrée.
2. **Vérifie si Python est déjà là** : tape `python3 --version` puis Entrée.
   - Si tu vois `Python 3.` suivi d'un numéro, c'est bon : passe directement à la partie 2.
   - Si une fenêtre te propose d'installer les « outils de développement en ligne de commande »,
     clique sur « Annuler » et continue ci-dessous : la version proposée est ancienne.
3. **Télécharge Python** sur le site officiel : https://www.python.org/downloads/
   Clique sur le gros bouton jaune « Download Python 3.x.x ».
4. **Installe-le** : ouvre le fichier `.pkg` téléchargé et clique sur « Continuer » jusqu'au bout.
5. **Étape indispensable** : ouvre le Finder, va dans « Applications », puis dans le dossier
   « Python 3.x », et double-clique sur **`Install Certificates.command`**.
   Sans ça, Python ne pourra pas télécharger les données sur internet
   (erreur `CERTIFICATE_VERIFY_FAILED`).
6. **Ferme et rouvre le Terminal**, puis retape `python3 --version` : tu dois voir le numéro de version.

Si tu utilises déjà Homebrew, `brew install python` fonctionne aussi.

## 2. Récupérer le didacticiel

- Sur la page GitHub du projet, clique sur le bouton vert « Code », puis sur « Download ZIP ».
- Double-clique sur le fichier ZIP pour le décompresser.
- Dans le Terminal, tape `cd ` (avec un espace après), fais glisser le dossier décompressé dans la
  fenêtre du Terminal, puis appuie sur Entrée. Tu es maintenant « dans » le dossier.

## 3. Ce qu'il faut

- Python 3.9 ou plus récent.
- Une connexion internet (pour les étapes 2 et 3 et les exercices).
- Aucune bibliothèque à installer : on n'utilise que ce qui est livré avec Python.

## 4. Comment lancer un fichier

Dans le Terminal, depuis le dossier du didacticiel, tape par exemple :

```
python3 etape1_les_bases.py
```

Lis le fichier dans un éditeur de texte (VS Code, TextEdit, gedit, Bloc-notes…) en même temps que tu le lances :
tout ce qui suit un `#` est une explication pour toi, Python l'ignore.

## 5. Le parcours

| Fichier | Ce que tu apprends |
|---|---|
| `etape1_les_bases.py` | afficher du texte, les variables, les listes, les boucles, les conditions, les dictionnaires |
| `etape2_recuperer_les_donnees.py` | télécharger des données open data et les regarder |
| `etape3_champions_de_judo.py` | filtrer les données pour ne garder que les champions de judo |

## 6. Les exercices

Dans les exercices, remplace les `___` par le bon code puis lance le fichier.
Chaque `___` a un indice juste au-dessus. Les exercices sont rangés du plus facile au plus difficile.

| Fichier | Difficulté | Le défi |
|---|---|---|
| `exercices/exercice1_les_francais.py` | ⭐ | afficher tous les médaillés français en judo |
| `exercices/exercice2_classement_des_pays.py` | ⭐⭐ | quel pays domine le judo ? |
| `exercices/exercice3_ton_sport.py` | ⭐⭐ | écrire une fonction pour n'importe quel sport |
| `exercices/exercice4_le_sport_roi.py` | ⭐⭐ | le judo est-il le sport qui rapporte le plus de médailles à la France ? |
| `exercices/exercice5_question_reponse.py` | ⭐⭐ | un programme qui te demande un pays et te répond |
| `exercices/exercice6_le_calendrier.py` | ⭐⭐⭐ | réparer les dates erronées des données et faire le calendrier des titres |
| `exercices/exercice7_par_categorie_de_poids.py` | ⭐⭐⭐ | trier les champions du plus léger au plus lourd |

Si tu bloques, les corrigés sont dans `exercices/solutions/`… mais essaie d'abord ! 😉

## 7. Si ça plante

C'est normal, ça arrive à tout le monde, tout le temps. Lis la **dernière ligne** du message d'erreur :

- `NameError: name '___' is not defined` → tu as oublié de remplacer un `___`.
- `IndentationError` → les espaces en début de ligne ne sont pas alignés. En Python, le décalage compte !
- `SyntaxError` → il manque souvent un `:`, une parenthèse ou un guillemet.
- `CERTIFICATE_VERIFY_FAILED` (sur Mac) → refais l'étape 5 de l'installation (`Install Certificates.command`).
- `URLError` → pas de connexion internet, ou le site est momentanément indisponible.
- `command not found: python3` → Python n'est pas installé, ou il faut fermer et rouvrir le Terminal.
