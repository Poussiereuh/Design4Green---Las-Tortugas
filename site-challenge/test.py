def type1(id_q):
    id = liste_question[id_q-1]["answer"].index(i)
    html = """
    <div id="type1" class="container">
        <h2>""" + str(liste_question[id_q-1]["id"])+" "+liste_question[id_q-1]["question"] + """</h2>"""

    for i in liste_question[id_q-1]["answer"]:
        html += """
    <p>
                <input type="radio"
                       name=" """ + str(liste_question[id_q-1]["id"]) + """ "
                       value=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(id) + """ "
                       id=" """ + str(id) + """ " required/>

                <label for=" """+ str(id) +""" ">""" + i + """</label>
            </p>
    """
    html += "</div>"
    return html

def type2(id_q):
    html = """
     <div id="type2" class="container">
        <h2>""" + liste_question[id_q-1]["question"] + """</h2>
        <p>
            <input type="text"
                   name=" """ + liste_question[id_q-1]["id"] + """ "
                   placeholder="Answer..." required/>
        </p>
    </div>
    """
    return html

def type3(id_q):
    answer_list = liste_question[id_q]["answer"]
    text_answer = liste_question[id_q]["textfield"]

    html = """
    <div id="type3" class="container">
        <h2>""" + liste_question[id_q]["question"] + """</h2>"""

    for i in answer_list:
        html += """
            <p>
                <input onclick="resetTxtField(['
        """
    for j in text_answer-1:
        html += answer_list.index(j) + "','"
        html += answer_list[len(text_answer)-1] + """'])"
                       type="radio"
                       name=" """ + str(liste_question[id_q]["id"]) + """ "
                       value=" """ + str(liste_question[id_q]["id"]) + ":" + str(answer_list.index(i)) + """ "
                       id=" """ + str(answer_list.index(i)) + """ " required/>
                <label for=" """ + str(answer_list.index(i)) + """ ">""" + i + """</label>
            </p>"""
        html += "</div>"
    return html

def type4(id_q):
    html = """
    <div id="type4" class="container">
        <h2>""" + liste_question[id_q-1]["question"] + """</h2>
    """

    for i in liste_question[id_q-1]["answer"]:
        id = liste_question[id_q-1].index(i)
        html += """
                <p>
                    <input type="checkbox"
                           name=" """ + liste_question[id_q-1]["id"] + """[]"
                           value=" """ + liste_question[id_q-1]["id"] +""":""" + str(id) + """ "
                           id=" """ + str(id) + """ "/>
                    <label for=" """ + str(id) + """ ">""" + i + """</label>
                </p>"""

        html += "</div>"
    return html

def type5(id_q):
    question_list = liste_question[id_q-1]["question"]
    answer_list = liste_question[id_q-1]["column"]

    html = """
    <div id="type5" class="container">
        <table style="width:100%">
             <tr>
               <td><h2>""" + liste_question[id_q-1]["question"] + """</h2></td>"""

    for j in answer_list:
        html += """
                   <td>
                       <input type="radio"
                          name=" """ + str(liste_question[id_q-1]["id"]) + """ "
                          value=" """ + str(liste_question[id_q-1]["id"]) + """:""" + str(answer_list.index(j)) + """ "
                          id=" """ + str(answer_list.index(j)) + """ "/>

                       <label for=" """ + str(answer_list.index(j)) + """ ">""" + j + """</label>
                   </td>"""

    html += """</tr>
    </table>
    </div>"""
    return html

def type6(id_q):
    question_list = liste_question[id_q-1]["question"]
    answer_list = liste_question[id_q-1]["column"]
    html = """
    <div id="type6" class="container">
        <table style="width:100%">
             <tr>
               <td><h2>""" + liste_question[id_q-1]["title"] + """</h2></td>
    """

    for j in answer_list:
        html += """
                   <td>
                       <input type="checkbox"
                          name="
        """
        html += str(liste_question[id_q-1]["id"])
        html += "value=" + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(j)) + "id="

        html += str(answer_list.index(j)) + "/>"

        html += "<label for=" + str(answer_list.index(j)) + '">' + j + "</label>"
        html += "</td>"

    html += """
        </tr>
            </table>
        </div>
    """
    return html

def type7(id_q):
    answer_list = liste_question[id_q-1]["answer"]
    text_answer = liste_question[id_q-1]["textfield"]
    html = """
    <div id="type7" class="container">
        <h2>""" + liste_question[id_q-1]["question"] + """</h2>
    """

    for i in answer_list:
        html += """
            <p>
                <input onclick="resetTxtField(['
                """

    for j in text_answer-1:
        html += answer_list.index(j) + "','"
        html += answer_list[len(text_answer)-1] + """'])"
                           type="checkbox"
                           name=" """ + liste_question[id_q-1]["id"] + """[]"
                           value=" """ + liste_question[id_q-1]["id"] + """:""" + answer_list.index(j) + """ "
                           id=" """ + answer_list.index(j) + """ " required/>

                    <label for=" """ + answer_list.index(j) + """ ">""" + j + """</label>
                </p>"""

    html += """</div>"""
    return html

def type8(id_q):
    answer_list = liste_question[id_q-1]["answer"]
    html = """
    <div id="type8" class="container">
        <h2>""" + liste_question[id_q-1]["question"] + """</h2>"""

    for i in answer_list:
        html += """
                <p>
                    <label for=" """ + answer_list.index(j) + """ ">""" + i + """</label>
                    <input type="text"
                           name=" """ + answer_list.index(j) + """ "
                           id=" """ + answer_list.index(j) + """ "
                           placeholder=" """ + j + """ " required/>
                </p>"""

    html += """</div>"""
    return html

def header():
    html = """
    <!DOCTYPE html>
    <html lang="fr">

    <head>
        <title>Las tortugas - </title>
        <meta charset="utf-8"  />
        <link rel="icon" type="image/png" href="/img/favicon.png"/>
        <meta name="description" content="" />
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>

    <body>
        <div class="head"></div>
        <div class="mainContainer">
    """
    return html

def intro():
    html = """
    <div class="container justify">
        <h2>Welcome to the survey design4green!</h2>
        <p>
            With the support of ADEME, the Ministry of Ecology, Energy and the Sea and the
            Ministry of Economy and Finance, the association AGIT (Alliance for Green IT) and
            the eco-organizations of the recycling network of Waste Electrical and Electronic
            Equipment (WEEE) organize a survey to assess the deposits of computer and office
            equipment present in companies and more generally on the maturity of companies in
            France in the use of eco-responsible digital services.
        </p>
        <p>
            The duration of the questionnaire is estimated at 15 minutes if you are able to
            answer questions directly.
        </p>
        <p>
            You can return at any time on the questionnaire, answer in several times, your
            previous answers are recorded. In case of modification, only the last answer will
            be taken into account.
        </p>
        <p>
            You can submit this questionnaire to several people in your organization. All you
            have to do is simply share the link to the questionnaire.
        </p>
        <p>
            Thank you for participating in this survey. Your answer is invaluable to us to
            constitute the most representative sample of the companies in France.
        </p>
        <button class="button">Start</button>
    </div>
    """
    return html

def startform():
    html = """
    <form method="post" action="">
    """

def footer():
    html = """
    <input class="submit" type="submit" value="Submit"/>
                <input class="button" type="submit" value="Next"/>
            </form>

            <div class="container">
                <h2>Thank you!</h2>
                <p>Thank you for your answers. Now, you can download your report.</p>
                <button class="button">Download</button>
            </div>
        </div>

        <script type="text/javascript" src="javascript.js"></script>
    </body>
    </html>
    """
    return html

def print_q(id_question, html):
    ret = ""
    if liste_question[id_question-1]["type"] == 1:
        html += type1(id_question)

    elif liste_question[id_question-1]["type"] == 2:
        html += type2(id_question)

    elif liste_question[id_question-1]["type"] == 3:
        html += type3(id_question)

    elif liste_question[id_question-1]["type"] == 4:
        html += type4(id_question)

    elif liste_question[id_question-1]["type"] == 5:
        html += type5(id_question)

    elif liste_question[id_question-1]["type"] == 6:
        html += type6(id_question)

    elif liste_question[id_question-1]["type"] == 7:
        html += type7(id_question)

    elif liste_question[id_question-1]["type"] == 8:
        html += type8(id_question)

    return html

def parcours_q(id_debut):
    liste_choix_deter = [4, 12, 13, 39, 62]
    html = header() + startform()
    for i in range(id_debut, len(liste_question)-1):
    if not i in liste_choix_deter:
    html += str(print_q(i+1, html))
    else:
    break

    html += footer()
    return html

if not form:
    html = intro() + parcours_q(0)
