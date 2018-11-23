#!/usr/bin/python3
# -*- coding: utf-8 -*
from random import randrange
# Print basic html header code
def display_intro_header():
	return """<!DOCTYPE html>
	<html lang="fr">
	<head>
		<title>Las tortugas: Online SURVEY</title>
		<meta charset="utf-8" />
		<meta name="description" content="text/html;" />
		<link rel="icon" href="favicon.ico"/>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
		<form method="post" action="/cgi-bin/new_fonctions.py">
		<div id="type1" class="container">
	"""

# Print intro message of the survey
def display_intro_msg():
	return """
	<h1>Las TORTUGAS SURVEY</h1>
	<p>Welcome to the online survey of TORTUGAS SURVEY team</p>
	<p> The main goal of this server is to gather your opinion on the subject XXX</p>
	<form action="/cgi-bin/index.py" method="post">
			<input type="text" name="email" value="" />
			<input type="submit" name="send" value="Rechercher">
	</form>
	"""

# To close the HTML page
def display_out_footer():
	return """<input type="submit" name="next" value="Next"/></div></form></body><footer></footer></html>"""

def type1(id_q):
	html = """
	<div id="type1" class="container">
		<h2>%s %s</h2>""" %(str(liste_question[id_q-1]["id"]), liste_question[id_q-1]["question"])

	for i in liste_question[id_q-1]["answer"]:
		html += """
		<p>
			<input type="radio"
					name=" """ + str(liste_question[id_q-1]["id"]) + """ "
					value=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(liste_question[id_q-1]["answer"].index(i)) + """ "
					id=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(liste_question[id_q-1]["answer"].index(i)) + """ " required/>

			<label for=" """+ str(liste_question[id_q-1]["id"]) + ":" + str(liste_question[id_q-1]["answer"].index(i)) +""" ">""" + i + """</label>
		</p>"""
	html += "</div>"
	return html

def type2(id_q):
	html = """
	<div id="type2" class="container">
	<h2>""" + str(liste_question[id_q-1]["id"]) + " " + str(liste_question[id_q-1]["question"]) + """</h2>
		<p>
			<input type="text"
				   name=" """ + str(liste_question[id_q-1]["id"]) + """ "
				   id=" """ + str(liste_question[id_q-1]["id"]) + """:0"
				   placeholder="Answer..." required/>
		</p>
	</div>
	"""
	return html

def type3(id_q):
	answer_list = liste_question[id_q-1]["answer"] #tableau des réponses
	text_answer = liste_question[id_q-1]["textfield"] #tableau des id des radio button avec textfield
	resetTxtField = ""
	for machin in text_answer:
		resetTxtField += "' "+str(liste_question[id_q-1]["id"])+":"+str(machin)+" ',"

	html = """
	<div id="type3" class="container">
		<h2>""" + str(liste_question[id_q-1]["id"]) + " " + str(liste_question[id_q-1]["question"]) + """</h2>"""

	for i in answer_list:
		html += """
			<p>
				<input onclick="resetTxtField([""" + resetTxtField + """])"
					   type="radio"
					   name=" """ + str(liste_question[id_q-1]["id"]) + """ "
					   value=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ "
					   id=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ " required/>
				<label for=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ ">""" + i + """</label>"""
		for pos in text_answer:
			if pos == answer_list.index(i):
				html += """<input onclick="setFocus(' """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ ')" id=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ :textfill" type="text" name="other"/>"""
		html += """</p>"""
	html = html.replace("',])", "'])")
	html += "</div>"
	return html

def type4(id_q):
	html = """
	<div id="type4" class="container">
		<h2>""" + str(liste_question[id_q-1]["id"]) + """ """ + str(liste_question[id_q-1]["question"]) + """</h2>
	"""

	for i in liste_question[id_q-1]["answer"]:
		id = liste_question[id_q-1]["id"]
		html += """
				<p>
					<input type="checkbox"
						   name=" """ + str(liste_question[id_q-1]["id"]) + """[]"
						   value=" """ + str(liste_question[id_q-1]["id"]) +""":""" + str(liste_question[id_q-1]["answer"].index(i)) + """ "
						   id=" """ + str(liste_question[id_q-1]["id"]) +""":""" + str(liste_question[id_q-1]["answer"].index(i)) + """ "/>
					<label for=" """ + str(liste_question[id_q-1]["id"]) +""":""" + str(liste_question[id_q-1]["answer"].index(i)) + """ ">""" + i + """</label>
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
			   <td><h2> """ + str(liste_question[id_q-1]["id"]) + """ """ + str(liste_question[id_q-1]["question"]) + """</h2></td>"""

	for j in answer_list:
		html += """
				   <td>
					   <input type="radio"
						  name=" """ + str(liste_question[id_q-1]["id"]) + """ "
						  value=" """ + str(liste_question[id_q-1]["id"]) + """:""" + str(answer_list.index(j)) + """ "
						  id=" """ + str(liste_question[id_q-1]["id"]) + """:""" + str(answer_list.index(j)) + """ "/>

					   <label for=" """ + str(liste_question[id_q-1]["id"]) + """:""" + str(answer_list.index(j)) + """ ">""" + j + """</label>
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
			   <td><h2>""" + str(liste_question[id_q-1]["title"]) + """</h2></td>
	"""

	for j in answer_list:
		html += """
				   <td>
					   <input type="checkbox"
						  name="
		"""
		html += str(liste_question[id_q-1]["id"]) + """ " """
		html += 'value=" ' + str(liste_question[id_q-1]["id"]) + ':' + str(answer_list.index(j)) + ' "id=" '

		html += str(answer_list.index(j)) + ' "/>'

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
	resetTxtField = ""
	for machin in text_answer:
		resetTxtField += "'"+str(machin)+"',"

	html = """
	<div id="type7" class="container">
		<h2>""" + str(liste_question[id_q-1]["id"]) + """ """ + str(liste_question[id_q-1]["question"]) + """</h2>
	"""

	for i in answer_list:
		html += """
			<p>
				<input onclick="resetTxtField([""" + resetTxtField + """])"
						   type="checkbox"
						   name=" """ + str(liste_question[id_q-1]["id"]) + """[]"
						   value=" """ + str(liste_question[id_q-1]["id"]) + """:""" + str(answer_list.index(i)) + """ "
						   id=" """ + str(answer_list.index(i)) + """ "/>

					<label for=" """ + str(answer_list.index(i)) + """ ">""" + i + """</label>"""
		for pos in text_answer:
			if pos == answer_list.index(i):
				html += """<input onclick="setFocus(' """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ ')" id=" """ + str(liste_question[id_q-1]["id"]) + ":" + str(answer_list.index(i)) + """ :textfill" type="text" name="other"/>"""
		html += """</p>"""
	html = html.replace("',])", "'])")
	html += """</div>"""
	return html

def type8(id_q):
	answer_list = liste_question[id_q-1]["answer"]
	html = """
	<div id="type8" class="container">
		<h2>""" + str(liste_question[id_q-1]["id"]) + """ """ + str(liste_question[id_q-1]["question"]) + """</h2>"""

	for i in answer_list:
		html += """
				<p>
					<label for=" """ + str(liste_question[id_q-1]["id"]) + ":" +str(answer_list.index(i)) + """ ">""" + i + """</label>
					<input type="number"
						   name=" """ + str(liste_question[id_q-1]["id"]) + ":" +str(answer_list.index(i)) + """ "
						   id=" """ + str(liste_question[id_q-1]["id"]) + ":" +str(answer_list.index(i)) + """ "
						   placeholder=" """ + i + """ " required/>
				</p>"""

	html += """</div>"""
	return html

def header():
	return """<!DOCTYPE html>
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

def intro():
	return """
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
		<form method="post" action="">
			<input class="button" name="intro" type="submit" value="Start!"/>
		</form>
	</div>
	"""

def startform():
	return """<form method="post" action="">"""

def footer(id):
	html = ''
	if id == None:
		pass

	elif id != None:
		html = """
					<input class="submit" type="submit" name="submit" value="Continue later"/>
					<input class="button" type="submit" name="next" value="Next"/>
					</form>
				   """
	elif id == 89:
		html = """
			<div class="container">
				<h2>Thank you!</h2>
				<p>Thank you for your answers. Now, you can download your report.</p>
			</div>
		</div>"""

	html += """<script type="text/javascript" src="javascript.js"></script>
	</body>
	</html>
	"""
	return html

def afficherFin():
	html = """<div class="container">
		<h2>Thank you!</h2>
		<p>Thank you for your answers. Now, you can download your report.</p>
	</div>
</div>"""
	print(html)

def goto(id_q, id_rep):
	if id_q == 4 and id_rep == 0:
		return 5
	elif id_q == 4 and id_rep == 1:
		return 12
	elif id_q == 12 and id_rep == 0:
		return 50
	elif id_q == 12 and id_rep == 1:
		return 13
	elif id_q == 13 and id_rep == 0:
		return 31
	elif id_q == 13 and id_rep == 1:
		return 14
	elif id_q == 39 and (id_rep == 0 or id_rep == 1):
		return 42
	elif id_q == 39 and id_rep == 2:
		return 40
	elif id_q == 62 and id_rep == 0:
		return 63
	elif id_q == 62 and id_rep == 1:
		return 70
	# elif id_q == 88:
	# 	return 89

def print_q(id_question, html):
	if liste_question[id_question-1]["type"] == 0:
		html = intro()

	elif liste_question[id_question-1]["type"] == 1:
		html = type1(id_question)

	elif liste_question[id_question-1]["type"] == 2:
		html = type2(id_question)

	elif liste_question[id_question-1]["type"] == 3:
		html = type3(id_question)

	elif liste_question[id_question-1]["type"] == 4:
		html = type4(id_question)

	elif liste_question[id_question-1]["type"] == 5:
		html = type5(id_question)

	elif liste_question[id_question-1]["type"] == 6:
		html = type6(id_question)

	elif liste_question[id_question-1]["type"] == 7:
		html = type7(id_question)

	elif liste_question[id_question-1]["type"] == 8:
		html = type8(id_question)
	return html

def parcours_q(id_debut):
	liste_choix_deter = [4, 12, 13, 39, 62]
	html = "" + header() + startform()
	if id_debut != 89:
		try:
			for qCourante in range(id_debut, len(liste_question)+1):
				html += str(print_q(qCourante, html))
				if qCourante in liste_choix_deter:
					break
		except:
			afficherFin()
	html += footer(id_debut)
	return html

def recup_valeurs(form):
	liste_tempo_csv = []
	id_rand = str(randrange(10000000000000, 99999999999999))

#Si le form n'est pas vide
	if form:
		if form.getvalue("intro") == "Start!":
			html = parcours_q(1)
		else:
			for i in form:
				try:
					if "Next" not in form[i].value.split(':')[0]:
						question = form[i].value.split(':')[0]
						try:
							reponse = form[i].value.split(':')[1]
						except IndexError:
							pass
						liste_tempo_csv.append(str(question) + ':' + str(reponse))
				except AttributeError:
					pass
			s = liste_tempo_csv
			fichier = open('/var/www/html/cgi-bin/save_form.csv', 'w')
			fichier.write(str(s))
			fichier.close()

			liste_tempo_csv.sort()
			#ajoute le rand en debut de liste
			liste_tempo_csv.insert(0, id_rand)
			id_last_question = liste_tempo_csv[len(liste_tempo_csv)-1].split(':')[0]
			id_last_response = liste_tempo_csv[len(liste_tempo_csv)-1].split(':')[1]
			valeur = int(id_last_question)
			mareponse = int(id_last_response)

			return parcours_q(goto(valeur, mareponse))
	else:
		return ""
