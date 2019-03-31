#!/usr/bin/python3
# coding=utf-8
from cgi import FieldStorage
from random import randrange
import json
import cgitb

cgitb.enable()

form = FieldStorage()
q0 = {
	"id" : 0
	}
q1 = {
	"id" : 1,
	"question" : "In which sector of activity is your company active? (linked with your APE code)",
	"type" : 1,
	"answer" : ["Industry",
				"Business",
				"Information and communication",
				"Other services activity",
				"All other activities (financial, agricultural activities ...)",
				"Construction",
				"Public sector",
				"Specialized",
				"Scientific and Technical or Administrative and Support Services Activities",
				"Real estate"
				]
	}
q2 = {
	"id" : 2,
	"question" : "What is the number of employees in your company on 18/12/31?",
	"type" : 1,
	"answer" : [
				"0",
				"1 to 2",
				"3 to 9",
				"10 to 49",
				"50 to 249",
				"250 to 4999",
				"More than 5000"
				]
	}
q3 = {
	"id" : 3,
	"question" : "What is the turnover of your company in the last fiscal year? (or annual budget for Public sector)",
	"type" : 1,
	"answer" : [
				"0 to 100Kâ‚¬",
				"100 to 500 Kâ‚¬",
				"500 to 2 Mâ‚¬",
				"2 to 10 Mâ‚¬",
				"10 to 50 Mâ‚¬",
				"More than 50 Mâ‚¬"
				]
	}
q4 = {
	"id" : 4,
	"question" : "Do you develop digital services for internal or external use (sales to customers)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No"
				]
	}
q5 = {
	"id" : 5,
	"question" : "What is the number of users of your digital services?",
	"type" : 2,
	"answer" : "text"
	}
q6 = {
	"id" : 6,
	"type" : 5,
	"question" : "Do you apply the rules and best practices for digital accessibility?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q7 = {
	"id" : 7,
	"type" : 5,
	"question" : "Have you optimized the states and printouts in your application tools (reduced number of pages when printing, ink consumption ...)?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q8 = {
	"id" : 8,
	"type" : 5,
	"question" : "Do you integrate the principles of the ecodesign of digital services?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q9 = {
	"id" : 9,
	"type" : 5,
	"question" : "Do you use a modular application architecture?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q10 = {
	"id" : 10,
	"type" : 5,
	"question" : "Do you use a modular application architecture?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q11 = {
	"id" : 11,
	"question" : "What is the overall storage volume of your corporate data (centralized on external hard drives, centralized server, NAS, SAN ...) in Terabytes (TB) useful?",
	"type" : 3,
	"textfield" : [2],
	"answer" : [
				"I don't know",
				"I do not want to answer",
				"TB"
				]
	}
q12 = {
	"id" : 12,
	"question" : "Do you have a server or do you only work with one or more workstations?",
	"type" : 1,
	"answer" : [
				"We work with workstation(s), without centralized physical server",
				"We have (at least) a centralized physical server"
				]
	}
q13 = {
	"id" : 13,
	"question" : "Do you have a dedicated room, simple room or cupboard with bay dedicated to your IT infrastructure?",
	"type" : 1,
	"answer" : [
				"A closet or a room without any specific system",
				"A dedicated room"
				]
	}
q14 = {
	"id" : 14,
	"question" : "Is your computer room in house or at a host?",
	"type" : 1,
	"answer" : [
				"Internal",
				"Host Member of the European Code of Conduct for Datacenters",
				"Non-adhering Host of the European Code of Conduct for Data Centers"
				]
	}
q15 = {
	"id" : 15,
	"question" : "What is the total area of your computer rooms (excluding technical infrastructure *)? (in m2)",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"mÂ²"
				"I don't know",
				"I do not want to answer"
				]
	}
q16 = {
	"id" : 16,
	"question" : "Do you know the PUE of your Data Center? (PUE : Power Usage Effectiveness)",
	"type" : 1,
	"answer" : [
				"Less than 1,6",
				"Between 1,6 and 2,1",
				"More than 2,1",
				"I don't know"
				]
	}
q17 = {
	"id" : 17,
	"question" : "What is the rate of charge or energy use of your computer rooms? (Rate = Electrical power absorbed by your IT equipment, divided by room capacity in kW, then multiplied by 100 (used energy / available energy))",
	"type" : 1,
	"answer" : [
				"100% - 90%",
				"90% - 60%",
				"Less than 60%",
				"I don't know"
				]
	}
q18 = {
	"id" : 18,
	"type" : 5,
	"question" : "Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q19 = {
	"id" : 19,
	"type" : 5,
	"question" : "The purchase of non-IT equipment from IT rooms (air conditioning, air treatment, inverters, etc.) according to energy efficiency criteria",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q20 = {
	"id" : 20,
	"type" : 5,
	"question" : """Implementing the good practices of the "European Code of Conduct for DataCenter?" """,
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q21 = {
	"id" : 21,
	"type" : 5,
	"question" : "Data center PUE tracking",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q22 = {
	"id" : 22,
	"type" : 5,
	"question" : "Regular monitoring of environmental indicators of computer rooms",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q23 = {
	"id" : 23,
	"type" : 5,
	"question" : "Environmental impact analysis of the datacenter in life cycle approach",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q24 = {
	"id" : 24,
	"type" : 5,
	"question" : "Optimizing the architecture and layout of rooms",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q25 = {
	"id" : 25,
	"type" : 5,
	"question" : "The urbanization of halls in hot / cold aisles",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q26 = {
	"id" : 26,
	"type" : 5,
	"question" : "Containment of air flows (corridors)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q27 = {
	"id" : 27,
	"type" : 5,
	"question" : "The use of natural cooling sources (freecooling)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q28 = {
	"id" : 28,
	"type" : 5,
	"question" : "Implementation of a heat recovery system for computer rooms (heating)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q29 = {
	"id" : 29,
	"type" : 5,
	"question" : "The set temperature in the cold corridor remains higher than 24 Â°",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q30 = {
	"id" : 30,
	"type" : 5,
	"question" : "The choice of a modular datacenter architecture",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q31 = {
	"id" : 31,
	"type" : 5,
	"question" : "Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q32 = {
	"id" : 32,
	"type" : 5,
	"question" : "Suspending network equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q33 = {
	"id" : 33,
	"type" : 5,
	"question" : "Pooling physical equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q34 = {
	"id" : 34,
	"type" : 5,
	"question" : "Uninstalling unnecessary infrastructure",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q35 = {
	"id" : 35,
	"type" : 5,
	"question" : "Traceability of material elements (CMDB)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q36 = {
	"id" : 36,
	"type" : 5,
	"question" : "The correct sizing of the servers in relation to their use",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q37 = {
	"id" : 37,
	"type" : 5,
	"question" : "Give priority to ASHRAE 2 compatible equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q38 = {
	"id" : 38,
	"type" : 5,
	"question" : "A procedure for provisioning and de-provisioning data-processing equipment in datacenters",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q39 = {
	"id" : 39,
	"question" : "Do you know the number of physical servers and virtual servers in your company?",
	"type" : 1,
	"answer" : [
				"No",
				"I do not want to answer",
				"Yes"
				]
	}
q40 = {
	"id" : 40,
	"question": "How many physical servers do you have?",
	"type": 2,
	"answer": "text"
	}
q41 = {
	"id" : 41,
	"question": "How many virtual servers do you have?",
	"type": 2,
	"answer": "text"
	}
q42 = {
	"id" : 42,
	"question": "How many virtual servers do you have?",
	"type" : 3,
	"textfield" : [0, 1],
	"answer": [
			"In %",
			"In quantity",
			"I do not want to answer",
			"I don't know"
			]
	}
q43 = {
	"id" : 43,
	"question": "What will be the evolution of your number of virtual servers for 2019? (in% or quantity)",
	"type" : 3,
	"textfield" : [0, 1],
	"answer": [
			"In %",
			"In quantity",
			"I do not want to answer"
			"I don't know"
			]
	}
q44 = {
	"id" : 44,
	"question" : "Has your company appointed a Green IT Manager / Digital Manager?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q45 = {
	"id" : 45,
	"question" : "Do you have a responsible digital strategy broken down into an action plan?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q46 = {
	"id" : 46,
	"question" : "Is Green IT a topic integrated into your CSR strategy?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q47 = {
	"id" : 47,
	"question" : "Do you regularly evaluate the environmental impacts of your information system?",
	"type" : 1,
	"answer" : [
				"Yes partially, including only equipment present in the company",
				"Yes totally, including our internal equipment and services hosted by third parties",
				"No",
				"I do not know"
				]
	}
q48 = {
	"id" : 48,
	"question" : "Do you have a team of competent referees on the topics of Green IT?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q49 = {
	"id" : 49,
	"question" : "Have you integrated Green IT into your business strategy",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q50 = {
	"id" : 50,
	"type" : 5,
	"question" : "Do you have those equipments in your compagny: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q51 = {
	"id" : 51,
	"type" : 5,
	"question" : "Fixed stations, workstations",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q52 = {
	"id" : 52,
	"type" : 5,
	"question" : "Laptops, digital tablets",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q53 = {
	"id" : 53,
	"type" : 5,
	"question" : "Small printers (<15kg, potentially used by a household)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q54 = {
	"id" : 54,
	"type" : 5,
	"question" : "Flat screen monitors",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q55 = {
	"id" : 55,
	"type" : 5,
	"question" : "Other flat screens (TV, projection screen, digital board ...)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q56 = {
	"id" : 56,
	"type" : 5,
	"question" : "CRT monitors (monitors or other)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q57 = {
	"id" : 57,
	"type" : 5,
	"question" : "Video projectors",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q58 = {
	"id" : 58,
	"type" : 5,
	"question" : "Mobile phones",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q59 = {
	"id" : 59,
	"type" : 5,
	"question" : "Fixed telephones (standalone not connected to such a standard)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q60 = {
	"id" : 60,
	"type" : 5,
	"question" : "Digital cameras",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q61 = {
	"id" : 61,
	"type" : 5,
	"question" : "Hard Disk Devices, Storage, Backup",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q62 = {
	"id" : 62,
	"question" : "Do you have other devices in your company? (Keyboards, mouse, graphic tablets, scanners, microphones, speakers, office equipment ...)",
	"type" : 1,
	"answer" : [
				"Yes",
				"No"
				]
	}
q63 = {
	"id" : 63,
	"type" : 5,
	"question" : "Regarding other devices, do you have in your company: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q64 = {
	"id" : 64,
	"type" : 5,
	"question" : "Keyboards",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q65 = {
	"id" : 65,
	"type" : 5,
	"question" : "Mouse",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q66 = {
	"id" : 66,
	"type" : 5,
	"question" : "Graphic Tablets",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q67 = {
	"id" : 67,
	"type" : 5,
	"question" : "Scanners",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q68 = {
	"id" : 68,
	"type" : 5,
	"question" : "Speakers",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q69 = {
	"id" : 69,
	"type" : 5,
	"question" : "Office Automation",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}
q70 = {
	"id" : 70,
	"question" : "Do you know the consumption of your workstation in kWh per year?",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"Yes (please specify how much in kWh / year)",
				"No"
				]

	}
q71 = {
	"id" : 71,
	"question" : "Do you track the energy consumption of your compagny activities?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q72 = {
	"id" : 72,
	"question" : "Do you know the share of IT and IT equipment in your company's total energy consumption?",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"Yes (please specify how much in %)",
				"No"
				]
	}
q73 = {
	"id" : 73,
	"question" : "Have you set up a power management system? (automatic shutdown / shutdown of workstations)",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q74 = {
	"id" : 74,
	"question" : "Do you use copiers from a repackaging industry (second-hand / second-hand)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q75 = {
	"id" : 75,
	"question" : "Do you consolidate individual printers to shared printers?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q76 = {
	"id" : 76,
	"question" : "Have you set up an identification system on printers (to trigger printing)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q77 = {
	"id" : 77,
	"question" : "What is the average life of your professional copier / MFP *? * MFP Multi Fonction Printer",
	"type" : 3,
	"textfield" : [2],
	"answer" : [
				"I do not know",
				"Do not want to answer",
				"x years (please specify)"
				]
	}
q78 = {
	"id" : 78,
	"type" : 5,
	"question" : "Are your printers set by default in eco mode? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q79 = {
	"id" : 79,
	"type" : 5,
	"question" : "Energy saving (Automatic standby)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q80 = {
	"id" : 80,
	"type" : 5,
	"question" : "Black and white by default",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q81 = {
	"id" : 81,
	"type" : 5,
	"question" :"Default duplex",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q82 = {
	"id" : 82,
	"type" : 5,
	"question" : "Default draft mode",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
q83 = {
	"id" : 83,
	"question" : "What is the number of pages printed / day / employee? (A4 equivalent)",
	"type" : 1,
	"answer" : [
				"Less than 10",
				"From 10 to 20",
				"From 20 to 30",
				"More than 30",
				"I don't know"
				]
	}
q84 = {
	"id" : 84,
	"question" : "Can you specify the number of cartridges / toners:",
	"type" : 8,
	"answer" : [
				"Cartridges used a year",
				"Cartridges stored in the average business",
				"Toners used a year",
				"Toners stored in the average business"
				]
	}
q85 = {
	"id" : 85,
	"question" : "Do you organize the separate collection of waste cartridges / toners?",
	"type" : 1,
	"answer" : [
				"Yes, to a repackaging industry",
				"Yes, towards a recycling channel (destruction)",
				"No no separate collection device is planned"
				]
	}
q86 = {
	"id" : 86,
	"question" : "Do you prefer the use of recycled paper?",
	"type" : 4,
	"answer" : [
				"Yes, our paper is made from virgin paste",
				"Yes, mixed paper",
				"Yes, 100\% recycled",
				"Yes, European Label",
				"I'm not paying attention"
				]
	}
q87 = {
	"id" : 87,
	"question" : "Do you choose certified paper?",
	"type" : 7,
	"textfield" : [4],
	"answer" : [
				"Yes, FSC",
				"Yes, PEFC",
				"Yes, Blue Angel",
				"Yes, European Label",
				"Yes, other",
				"I'm not paying attention"
				]
	}
q88 = {
	"id" : 88,
	"question" : "Do you organize the separate collection of waste paper for recycling?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}
liste_question = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, q66, q67, q68, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88]
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
		<form method="post" action="">
		<div id="type1" class="container">
	"""

# Print intro message of the survey
def display_intro_msg():
	return """
	<h1>Las TORTUGAS SURVEY</h1>
	<p>Welcome to the online survey of TORTUGAS SURVEY team</p>
	<p> The main goal of this server is to gather your opinion on the subject XXX</p>
	<form action="" method="post">
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
	return """
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

def type3(id_q):
	answer_list = liste_question[id_q-1]["answer"] #tableau des rÃ©ponses
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
		<h2>Welcome to the Design4Green survey!</h2>
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
			<input name="email" type="email" placeholder="Email" required/>
			<input class="button" name="intro" type="submit" value="Start!"/>
		</form>
	</div>
	"""

def startform():
	return """<form method="post" action=""><input name="email" type="hidden" value='""" + str(form.getvalue("email")) + """'/>"""

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

def recup_valeurs():

#Si le form n'est pas vide
	if form:
		if form.getvalue("intro") == "Start!":
			html = parcours_q(1)
		else:
			email = form.getvalue("email")
			for i in form:
				try:
					if "Next" not in form[i].value.split(':')[0]:
						question = form[i].value.split(':')[0]
						try:
							reponse = form[i].value.split(':')[1]
						except IndexError:
							pass
						string_to_write = """ {""" + str(email) + """[" """ + str(question) + """ ", " """ + str(reponse) + """ "]} """
				except AttributeError:
					pass
<<<<<<< HEAD
			with open('save_form.json', 'a', encoding="UTF-8") as file:
				file.dumps(string_to_write)

=======

			liste_tempo_csv.sort()
			#ajoute le rand en debut de liste
			liste_tempo_csv.insert(0, id_rand)
>>>>>>> master
			id_last_question = liste_tempo_csv[len(liste_tempo_csv)-1].split(':')[0]
			id_last_response = liste_tempo_csv[len(liste_tempo_csv)-1].split(':')[1]
			valeur = int(id_last_question)
			mareponse = int(id_last_response)

			return parcours_q(goto(valeur, mareponse))
	else:
		return ""

############
#MAIN
#############
html = recup_valeurs()

if form.getvalue("intro") == "Start!":
<<<<<<< HEAD
	#with open('save_form.json', 'r', encoding="UTF-8") as f:

	f = open("save_form.json","r")
	datas = f.read()
	f.close()

	variable_get = form.getvalue("email")
	print(datas[str(variable_get)]["question"])

	if datas[str(variable_get)]["question"]:
		last_couple = datas[variable_get][len(datas[variable_get])-1]
		question_id = last_couple[0]

		if int(question_id) == 88:
			parcours_q(89)
		else:
			parcours_q(int(question_id))
	else:
		with open('save_form.json', 'a', encoding="UTF-8") as file:
			file.dumps(str(variable_get))
		html = parcours_q(1)
=======

	email_renseignee = form.getvalue("email")
	html = parcours_q(1)
>>>>>>> master

elif form.getvalue("next") != "Next":
	html = header() + intro()

print(html)
