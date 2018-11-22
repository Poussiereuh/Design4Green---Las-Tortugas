#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi

q1 = {
    "question": "Êtes-vous un homme ou une femme ?",
    "type": 1,
    "answer": ["Homme", "Femme"]
}


q2 = {
    "question": "Comment vous appelez-vous ?",
    "type": 2
}


liste_q = [q1, q2]

def header():
    html = """<!DOCTYPE html>
            <html lang="fr">

            <head>
            <title>An HTML standard template</title>
            <meta charset="utf-8" />
            <link rel="icon" type="image/png" href="/img/favicon.png"/>
            <meta name="description" content="" />
            </head>

            <body>"""

    return html

def footer():
    html = """<input type="submit" name="next" value="Next"/></div></form></body><footer></footer></html>"""
    return html

def type_1(dictionnaire_q):
    html = """<p><form action="/cgi-bin/index.py" method="post">"""
    html += """<h2>"""+dictionnaire_q["question"]+"""</h2>"""
    for questions in dictionnaire_q["answer"]:
        html += """<input type="radio" name='"""+dictionnaire_q["question"]+"""' value='"""+str(dictionnaire_q["answer"].index(questions))+"""' id="lala" required <label for="">"""+questions+"""</label>"""
    html += """</form></p>"""

    return html

form = cgi.FieldStorage()

if form:
    print(form)
    #html = header()+type_1(liste_q[id_req_pre])+footer()
else:
    html = header()+type_1(liste_q[0])+footer()

print(html)
