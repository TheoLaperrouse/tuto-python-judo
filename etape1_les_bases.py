# ÉTAPE 1 : les bases de Python, version judo
# Lance ce fichier avec :  python3 etape1_les_bases.py
#
# Tout ce qui suit un # est un commentaire : Python l'ignore, c'est juste pour toi.


# --- 1. Afficher du texte ---------------------------------------------------
# print() affiche ce qu'on lui donne entre parenthèses.
# Le texte se met entre guillemets.

print("Hajime ! Bienvenue dans ton premier programme Python.")
print()


# --- 2. Les variables --------------------------------------------------------
# Une variable, c'est une boîte avec une étiquette : on y range une valeur
# pour la réutiliser plus tard. Le signe = veut dire « range dans ».

champion = "Teddy Riner"
titres_individuels = 3
titres_par_equipe = 2

# On peut faire des calculs avec les nombres :
total = titres_individuels + titres_par_equipe

# Une « f-string » (le f devant les guillemets) permet de glisser
# des variables dans un texte, entre accolades { }.
print(f"{champion} a remporté {total} médailles d'or olympiques.")
print()


# --- 3. Les listes -----------------------------------------------------------
# Une liste range plusieurs valeurs dans l'ordre, entre crochets [ ].

ceintures = ["blanche", "jaune", "orange", "verte", "bleue", "marron", "noire"]

print(f"Il y a {len(ceintures)} couleurs de ceinture.")   # len() = la longueur
print(f"La première est {ceintures[0]}.")                 # on compte à partir de 0 !
print(f"La dernière est {ceintures[-1]}.")                # -1 = la dernière
print()


# --- 4. Les boucles ----------------------------------------------------------
# « for » répète des instructions pour chaque élément d'une liste.
# Les lignes décalées (4 espaces) sont celles qui se répètent.

print("Le parcours d'un judoka :")
for couleur in ceintures:
    print(f"  - ceinture {couleur}")
print()


# --- 5. Les conditions -------------------------------------------------------
# « if » (si), « elif » (sinon si), « else » (sinon) permettent de prendre
# des décisions. Ici, on cherche la catégorie de poids d'un judoka homme.
# Essaie de changer le poids et relance le fichier !

poids = 85

if poids <= 60:
    categorie = "-60 kg"
elif poids <= 66:
    categorie = "-66 kg"
elif poids <= 73:
    categorie = "-73 kg"
elif poids <= 81:
    categorie = "-81 kg"
elif poids <= 90:
    categorie = "-90 kg"
elif poids <= 100:
    categorie = "-100 kg"
else:
    categorie = "+100 kg"

print(f"Un judoka de {poids} kg combat dans la catégorie {categorie}.")
print()


# --- 6. Les dictionnaires ----------------------------------------------------
# Un dictionnaire range des valeurs sous forme « clé : valeur », entre { }.
# C'est comme une fiche d'identité. Retiens bien ce format : les données
# qu'on va télécharger à l'étape 2 ressemblent exactement à ça !

judoka = {
    "nom": "Clarisse Agbegnenou",
    "pays": "France",
    "categorie": "-63 kg",
}

print(f"{judoka['nom']} ({judoka['pays']}) combat en {judoka['categorie']}.")
print()
print("Matte ! Fin de l'étape 1. Passe à l'étape 2 : python3 etape2_recuperer_les_donnees.py")
