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
    <form action="/cgi-bin/index.py" method="post">
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
        <form method="post" action="/cgi-bin/index.py">
        <div id="type1" class="container">
        <h2>
        """
    html += "id: "+str(current_question["id"])+" "+current_question["question"]
    html += "</h2><p>"

    # Add many radio buttons as needed
    for i in answer_list:
        id = answer_list.index(i)
        html +='<input type="radio" name=' + i
        html += 'value=' + str(current_question["id"]) + str(id)
        html += 'id="' + str(id) + '" required/>'
        html += '<label for=' + str(id) + '>' + i + '</label>'
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

    answer_list = current_question["answer"]
    text_answer = current_quesion["textfield"]

    html = """
        <form method="post" action="">
        <div id="type8" class="container">
        <h2>
        """
    html += current_question["question"]
    html += "</h2>"
    for i in answer_list:
        html += """
                <p>
                <input onclick="resetTxtField(idTxtFieldAssocie)"
                type="radio"
                name="
                """
        html += i
        html += """
                "
                value="
                """
        html += i + ":" + answer_list[i]
        html += """
                "
                id="
                """
        html += answer_list[i]
        html += """
                " required/>
                <label for="
                """
        html += answer_list[i]
        html += """
                ">
                """
        html += answer_list[i]
        html += "</label>"
        if i in text_answer :
            html += """
            <input onclick="resetRadioFocus(this.id)"
            id="
            """
            html += answer_list[i]
            html += """
                   :textill" type="text" name="other"/>
                    """
        html += "</p>"

    html += "</div>"

    return html

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
        html += '<input type="checkbox" name=' + i
        html += 'value=' + current_question["id"] + ":" + id
        html += 'id="' + id + '"/>'
        html += '<label for=' + id + '>' + i + '</label>'
        html+="</p>"

    return html

# Type 5: Tableau single
def display_question_type_5(current_question):

    question_list = current_question["question"]
    answer_list = current_question["column"]

    html = """
        <form method="post" action="">
        <div id="type5" class="container">
        <h2>{That is the title}</h2>
        <table style="width:100%">
        """

    for i in question_list:
        html +="""
            <tr>
            <td><h2>
        """
        html += current_question["title"]
        html += "</h2></td>"
        for j in answer_list:
            html += """
                    <td>
                    <input type="radio"
                    name="
                    """
            html += int(current_question["id"] + i + 1)
            html += """
                    "
                    value = "
                    """
            html += int(current_question["id"] + i + 1) + ":" + answer_list[j]
            html += """
                    "
                    id="
                    """
            html += answer_list[j]
            html += """
                    "/>
                    <label for="
                    """
            html += answer_list[j]
            html += ">" + answer_list[j] + "</label></td>"
        html += "</tr>"
    html += "</table></div>"

    return html

# Type 6: Tableau multiple
def display_question_type_6(current_question):

    question_list = current_question["question"]
    answer_list = current_question["column"]

    html = """
        <form method="post" action="">
        <div id="type5" class="container">
        <h2>{That is the title}</h2>
        <table style="width:100%">
        """

    for i in question_list:
        html +="""
            <tr>
            <td><h2>
        """
        html += current_question["title"]
        html += "</h2></td>"
        for j in answer_list:
            html += """
                    <td>
                    <input type="checkbox"
                    name="
                    """
            html += int(current_question["id"] + i + 1)
            html += """
                    "
                    value = "
                    """
            html += int(current_question["id"] + i + 1) + ":" + answer_list[j]
            html += """
                    "
                    id="
                    """
            html += answer_list[j]
            html += """
                    "/>
                    <label for="
                    """
            html += answer_list[j]
            html += ">" + answer_list[j] + "</label></td>"
        html += "</tr>"
    html += "</table></div>"

    return html

#Type 7: QCM + text field
def display_question_type_7(current_question):

    return current_question["question"] + "HTML"

#Type 8: Multiple text fields
def display_question_type_8(current_question):

    answer_list = current_question["answer"]
    html = """
        <form method="post" action="">
        <div id="type8" class="container">
        <h2>
        """
    html += current_question["question"]
    html += "</h2>"
    for i in answer_list:
        html += """
                <p>
                <label for="
                """
        html += i
        html += """
                ">
                """
        html += answer_list[i]
        html += """
                </label>
                <input type="text"
                name="
                """
        html += i
        html += """
                "
                placeholder="Answer..." required/>
                </p>
                """
    html += "</div>"

    return html

# How any
