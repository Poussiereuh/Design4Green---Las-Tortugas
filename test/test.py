#!/usr/bin/python3
# -*- coding: utf-8 -*
import cgi
import json

dictionnaire_resultats = {}
compteur = 0
trouve = False
form = cgi.FieldStorage()

if str(form) == 'FieldStorage(None, None, [])':
    trouve = False
    pass
else:
    trouve = True
    radio = form.getvalue('radio')
    checkbox = form.getvalue('checkbox[]')
    response = radio.split(":")

print("Content-type: text/html\n")
if trouve == False:
    html = """
     <!DOCTYPE html>
     <html lang="fr">

     <head>
     	<title>An HTML standard template</title>
     	<meta charset="utf-8"  />
             <link rel="icon" type="image/png" href="/img/favicon.png"/>
             <meta name="description" content="" />
     </head>

     <body>

         <form method="post" action="/cgi-bin/test.py">
             <p>
                 <input type="radio" name="radio" value="1:0" required/> rep1
             </p>
             <p>
                 <input type="radio" name="radio" value="1:1"/> rep2
             </p>
             <p>
                 <input type="radio" name="radio" value="1:2"/> rep3
             </p>
             <p>
                 <input type="checkbox" name="checkbox[]" value="2:0"/> rep4
             </p>
             <p>
                 <input type="checkbox" name="checkbox[]" value="2:1"/> rep5
             </p>
             <p>
                 <input type="checkbox" name="checkbox[]" value="2:2"/> rep6
             </p>
             <p>
                 <input type="text" name="text" required/> rep7
             </p>
             <p>
                 <input type="submit" />
                 <input type="reset" />
             </p>
         </form>

     </body>
     </html>

    """
#Si trouve = True on affiche une page HTML avec les champs demand�s dans le TP + les valeurs des variables via une boucle (Si il y a plusieurs r�sultats)
elif trouve == True:

    html = "Question n "+response[0]+" Reponse : "+response[1]+"<br>"
    for c in checkbox:
        html += "Question n "+c.split(':')[0]+" Reponse "+c.split(':')[1]+"<br />";

    print(form)
    compteur = 0


#On affiche le code HTML en entier
print(html)
