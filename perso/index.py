#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi

q1 = {
    "id": 0,
    "question": "Etes-vous un homme ou une femme ?",
    "type": 1,
    "answer": ["Homme", "Femme"]
}


q2 = {
    "id": 1,
    "question": "Comment vous appelez-vous ?",
    "type": 2
}

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

def type_x(dictionnaire_q):
    if dictionnaire_q["type"] == 1:
        html = """<p><form action="/cgi-bin/index.py" method="post">"""
        html += """<h2>"""+dictionnaire_q["question"]+"""</h2>"""
        for questions in dictionnaire_q["answer"]:
            html += """<input type="radio" name='"""+dictionnaire_q["question"]+"""' value='"""+str(dictionnaire_q["id"])+""":"""+str(dictionnaire_q["answer"].index(questions))+"""' id="lala" required <label for="">"""+questions+"""</label></p>"""
    elif dictionnaire_q["type"] == 2:
        html = """<p><form action="/cgi-bin/index.py" method="post">"""
        html += """<h2>"""+dictionnaire_q["question"]+"""</h2>"""
        html += """<input type="text" name='"""+dictionnaire_q["question"]+"""' placeholder="Answer..." required/><p>"""

    return html

form = cgi.FieldStorage()
liste_q = [q1, q2]

if form:
    # dict_tempo_csv = {}
    list_tempo = []
    # for i in form:
    #     dict_tempo_csv[i] = form[i].value.split(':')
    # dict_tempo_csv.pop("next")

    for i in form:
        list_tempo.append(i)
        list_tempo.append(form[i].value.split(':'))

    id_req_pre = int(list_tempo[1][0])

    html = header()+type_x(liste_q[id_req_pre+1])+footer()
else:
    html = header()+type_x(liste_q[0])+footer()

print(html)
