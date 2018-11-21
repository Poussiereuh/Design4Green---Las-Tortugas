#!/usr/bin/python3
# -*- coding: utf-8 -*

# Print basic html code
def display_intro_header():
    html = """<!DOCTYPE html>
    <html lang="fr">

    <head>
    <title>Online Survey: LAS TORTUGAS</title>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="/img/favicon.png"/>
    <meta name="description" content="" />
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
    html="<form><p>" + current_question["question"]

    # Add many radio buttons as needed
    for i in answer_list:
        html += answer_list[i]

    # html += END OF FORM

    #
    return html

# Type 2: Text field question
def display_question_type_2(current_question):

    return current_question["question"] + "HTML"


# Type 3: Single Choice + Text field
def display_question_type_3(current_question):

    return current_question["question"] + "HTML"


# Type 4: Multiple choice
def display_question_type_4(current_question):

    return current_question["question"] + "HTML"


# Type 5: Tableau single
def display_question_type_5(current_question):

    return current_question["question"] + "HTML"


# Type 6: Tableau multiple
def display_question_type_6(current_question):

    return current_question["question"] + "HTML"


#Type 7: QCM + text field
def display_question_type_7(current_question):

    return current_question["question"] + "HTML"


# How any
