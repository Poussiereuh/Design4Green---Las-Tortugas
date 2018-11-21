#!/usr/bin/python3
# -*- coding: utf-8 -*
import cgi
import json

#Définition du dictionnaire qui contiendra les valeurs à afficher
dictionnaire_resultats = {}
compteur = 0

#Ouverture de la BDD .json et attribution de la valeur à la variable 'datas'
with open('bdd.json', 'r') as f:
    datas = json.load(f)
print(datas)
#Importation de la fonction gérant les formulaires
form = cgi.FieldStorage()

#On commence à afficher du HTML
print("Content-type: text/html\n")

#On récupère la valeur dans le champ "name" (Si aucune valeur, v vaut None)
v = form.getvalue("name")

#Si v n'est pas égal à None, on passe la valeur de la chaine de caractère en miniscule avec la méthode .lower()
#Puis on cherche le nombre d'occurence de la valeur dans la bdd importée, on attribut la valeur retournée à la variable "compteur"
if v != None:
    v.lower()
    compteur = str(datas).count(v)

#Si le compteur est différent de 0 (Et donc que v n'est pas égal à None), trouve = True + initialisation du compteur i
if compteur != 0:
    trouve = True
    i = 0
#On récupère les valeurs des valeurs du fichier bdd.json qui est un dictionnaire de dictionnaire via une boucle for
    for recup_dict in datas.values():
        for recup_valeur in recup_dict.values():
#Si la valeur récupérée est égale à la valeur récupérée dans le champ, on récupère toutes les infos et on incrémente 1 au compteur
#afin de créer différents champs dans le dictionnaire si jamais il y a plusieurs résultats
            if recup_valeur == v:
                dictionnaire_resultats["prenom"+str(i)] = str(recup_dict['prenom'])
                dictionnaire_resultats["nom"+str(i)] = str(recup_dict['nom'])
                dictionnaire_resultats["promo"+str(i)] = str(recup_dict['promo'])
                dictionnaire_resultats["adresse"+str(i)] = str(recup_dict['adresse'])
                dictionnaire_resultats["cp"+str(i)] = str(recup_dict['cp'])
                dictionnaire_resultats["ville"+str(i)] = str(recup_dict['ville'])
                dictionnaire_resultats["photo"+str(i)] = '"'+str(recup_dict['photo'])+'"'
                recup_dict['compteur'] = recup_dict['compteur'] + 1
                dictionnaire_resultats["compteur"+str(i)] = recup_dict['compteur']
                i+=1

#On renvoie la BDD modifiée avec le compteur
    with open('bdd.json', 'w') as outfile:
        json.dump(datas, outfile, indent=4, ensure_ascii=False)

#Si le compteur vaut 0 et que donc, il n'a rien trouvé, trouve = False
else:
    trouve = False

#Si trouve = False on affiche la page html de base avec le formulaire (page d'accueil par défaut)
if trouve == False:
    html = """<!DOCTYPE html>
    <meta charset="utf-8" />
    <head>
        <title>Green IT</title>
    </head>
    <body style="text-align:center">
        <img src="images/300x100.jpg" alt="cat">
        <form action="/index.py" method="post">
            <input type="text" name="name" value="" />
            <input type="submit" name="send" value="Rechercher">
        </form>
    </body>
    <footer>
    <span><a style="text-decoration: none;" href='/index.py'>Mentions legales</a></span>
    </footer>
    </html>
    """
#Si trouve = True on affiche une page HTML avec les champs demandés dans le TP + les valeurs des variables via une boucle (Si il y a plusieurs résultats)
elif trouve == True:

    html = """<!DOCTYPE html>
    <meta charset="utf-8" />
    <head>
        <title>Green IT</title>
    </head>
    <body style="text-align:center">"""
    for nbr in range(0, compteur):
        html = html + """
        <img src="""+dictionnaire_resultats["photo"+str(nbr)]+"""> <br/><br/><br/>
        <b>Nom :</b> """+dictionnaire_resultats["nom"+str(nbr)].capitalize()+""" <br/>
        <b>Prenom :</b> """+dictionnaire_resultats["prenom"+str(nbr)].capitalize()+""" <br/>
        <b>Promotion :</b> """+dictionnaire_resultats["promo"+str(nbr)].capitalize()+""" <br/>
        <b>Adresse :</b> """+dictionnaire_resultats["adresse"+str(nbr)].capitalize()+""" <br/>
        <b>Code Postal :</b> """+dictionnaire_resultats["cp"+str(nbr)].capitalize()+""" <br/>
        <b>Ville :</b> """+dictionnaire_resultats["ville"+str(nbr)].capitalize()+""" <br/>
        <b>Compteur :</b> """+str(dictionnaire_resultats["compteur"+str(nbr)])+""" <br/>
        ---------------------------------- <br/>"""
    html = html + """
    </body>
    <footer>
    <span><a style="text-decoration: none;" href='/index.py'>Mentions legales</a></span>
    </footer>
    </html>
    """
    compteur = 0


#On affiche le code HTML en entier
print(html)
