#!/usr/bin/python3
# -*- coding: utf-8 -*

# Print basic html header code
def display_intro_header():

    html = """<!DOCTYPE html>
    <html lang="fr">
    <head>
    <title>Las tortugas: Online SURVEY</title>
    <meta charset="utf-8" />
    <meta name="description" content="" />
    <link rel="icon" type="image/png" href="/img/favicon.png"/>
    <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
    """
    return html


# Print intro message of the survey
def display_intro_msg():
    html = """
    <h1>Las TORTUGAS SURVEY</h1>
    <p>Welcome to the online survey of TORTUGAS SURVEY team</p>
    <p> The main goal of this server is to gather your opinion on the subject XXX</p>
    <form action="/index.py" method="post">
            <input type="text" name="email" value="" />
            <input type="submit" name="send" value="Rechercher">
    </form>
    """
    return html


# To close the HTML page
def display_out_footer():
    html ="""
    </body>
    <footer>
    </html/>
    """
    return html


# Determine the type of question to choose the right display
def determine_question_type(current_question):
    return current_question["type"]

# Type 1: Single choice question
def display_question_type_1(current_question):

    answer_list = current_question["answer"]

    # Begin of html form
    html="""
        <form method="post" action="">
        <div id="type1" class="container">
        <h2>
        """
    html += current_question["question"]
    html += "</h2><p>"

    # Add many radio buttons as needed
    for i in answer_list:
        id = answer_list.index['i']
        html +='<input type="radio" name=' + i
        html += 'value=' + current_question["id"] + id
        html += 'id="' + id + '" required/>'
        html += '<label for=' + id + '>' + i + '</label>'
    html+="</p>"
    html+="""<input type="submit" name="next" value="Next"/>"""

    return html

# Type 2: Text field question
def display_question_type_2(current_question):

    html = """
        <form method="post">
        <div id="type2" class="container">
        <h2>
        """
    html += current_question[1]
    html += """
            </h2>
            <p>
            <input type="text" name=
            """
    html += current_question[0]
    html += """
        " placeholder="Answer..." required/>
        </p>
        </div>
        """
    return html


# Type 3: Single Choice + Text field
def display_question_type_3(current_question):

    return current_question["question"] + "HTML"

# Type 4: Multiple choice
def display_question_type_4(current_question):

    answer_list = current_question["answer"]

    html="""
        <form method="post" action="">
        <div id="type4" class="container">
        <h2>
        """
    html += current_question["question"]
    html += "</h2><p>"

    for i in answer_list:
        id = answer_list.index['i']
        html +='<input type="checkbox" name=' + i
        html += 'value=' + current_question["id"] + id
        html += 'id="' + id + '"/>'
        html += '<label for=' + id + '>' + i + '</label>'
        html+="</p>"

    return html

# Type 5: Tableau single
def display_question_type_5(current_question):

    return current_question["question"] + "HTML"


# Type 6: Tableau multiple
def display_question_type_6(current_question):

    return current_question["question"] + "HTML"


#Type 7: QCM + text field
def display_question_type_7(current_question):

    return current_question["question"] + "HTML"

#Type 8: Multiple text fields
def display_question_type_8(current_question):

    return current_question["question"] + "HTML"

# How any
