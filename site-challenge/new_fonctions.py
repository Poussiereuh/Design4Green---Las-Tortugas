#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi

liste_choix_deter = [4, 12, 13, 39, 62]

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
				"0 to 100K€",
				"100 to 500 K€",
				"500 to 2 M€",
				"2 to 10 M€",
				"10 to 50 M€",
				"More than 50 M€"
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
	"title" : "Ecoconception good practices",
	"type" : 5,
	"question" : [
				"Do you apply the rules and best practices for digital accessibility?",
				"Have you optimized the states and printouts in your application tools (reduced number of pages when printing, ink consumption ...)?",
				"Do you integrate the principles of the ecodesign of digital services?",
				"Do you use a modular application architecture?",
				"Do you do a design review at the end of your application's development?"
				],

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
				"We work with workstation (s), without centralized physical server",
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
				"m²"
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
	"title" : "Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"type" : 5,
	"question" : [
				"The purchase of non-IT equipment from IT rooms (air conditioning, air treatment, inverters, etc.) according to energy efficiency criteria",
				"Implementing the good practices of the '"'European Code of Conduct for DataCenter?'"'",
				"Data center PUE tracking",
				"Regular monitoring of environmental indicators of computer rooms",
				"Environmental impact analysis of the datacenter in life cycle approach",
				"Optimizing the architecture and layout of rooms",
				"The urbanization of halls in hot / cold aisles",
				"Containment of air flows (corridors)",
				"The use of natural cooling sources (freecooling)",
				"Implementation of a heat recovery system for computer rooms (heating)",
				"The set temperature in the cold corridor remains higher than 24 °",
				"The choice of a modular datacenter architecture"
				],
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}


q31 = {
	"id" : 31,
	"Title" : "Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"type" : 5,
	"questions" : [
					"Suspending network equipment",
					"Pooling physical equipment",
					"Uninstalling unnecessary infrastructure",
					"Traceability of material elements (CMDB)",
					"The correct sizing of the servers in relation to their use",
					"Give priority to ASHRAE 2 compatible equipment",
					"A procedure for provisioning and de-provisioning data-processing equipment in datacenters"
				],
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
	"title" : "Do you have those equipments in your compagny: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"type" : 5,
	"question" : [
				"Fixed stations, workstations",
				"Laptops, digital tablets",
				"Small printers (<15kg, potentially used by a household)",
				"Flat screen monitors",
				"Other flat screens (TV, projection screen, digital board ...)",
				"CRT monitors (monitors or other)",
				"Video projectors",
				"Mobile phones",
				"Fixed telephones (standalone not connected to such a standard)",
				"Digital cameras",
				"Hard Disk Devices, Storage, Backup"
				],
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
	"title" : "Regarding other devices, do you have in your company: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"type" : 5,
	"question" : [
				"Keyboards",
				"Mouse",
				"Graphic tablets",
				"Scanners",
				"Speakers",
				"Office automation"
				],
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
	"title" : "Are your printers set by default in eco mode? Especially :",
	"type" : 5,
	"question" : [
				"Energy saving (Automatic standby)",
				"Black and white by default",
				"Default duplex",
				"Default draft mode"
				],
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
	"answer" : [
				"Yes, FSC",
				"Yes, PEFC",
				"Yes, Blue Angel",
                "Yes, European Label",
                "I'm not paying attention",
                "Yes, other"
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

liste_question = [q1, q2, q3, q4, q5, q6, q6, q11, q12, q13, q14, q15, q16, q17, q18, q31, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q62, q63, q70, q71, q72, q73, q74, q75, q76, q77, q78, q83, q84, q85, q86, q87, q88]

def goto(id_q, rep=''):
    if id_q == 0:
        return 0
    elif id_q == 4 and rep == 'Yes':
        return 5
    elif id_q == 4 and rep == 'No':
        return 12
    elif id_q == 12 and rep == 'We work with workstation (s), without centralized physical server':
        return 50
    elif id_q == 12 and rep == 'We have (at least) a centralized physical server':
        return 13
    elif id_q == 39 and (rep == 'No' or rep == 'I do not want to answer'):
        return 42
    elif id_q == 39 and rep == 'Yes':
        return 40
    elif id_q == 62 and rep == 'Yes':
        return 63
    elif id_q == 62 and rep == 'No':
        return 70


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
	<form method="post" action="/cgi-bin/new_fonctions.py">
	<div id="type1" class="container">
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
    html = """<input type="submit" name="next" value="Next"/></div></form></body><footer></footer></html>"""
    return html




def print_q(id_q, html):

#Type 1 code
    if liste_question[id_q-1]["type"] == 1:
        # Begin of html form
        html="""
		    <h2>
            """
        html += "id: "+str(liste_question[id_q-1]["id"])+" "+liste_question[id_q-1]["question"]
        html += "</h2><p>"

        # Add many radio buttons as needed
        for i in liste_question[id_q-1]["answer"]:
            id = liste_question[id_q-1]["answer"].index(i)
            html +='<input type="radio" name="' + liste_question[id_q-1]["question"]
            html += '" value="' + str(liste_question[id_q-1]["id"]) + ':' +str(id)
            html += '" id="' + str(liste_question[id_q-1]["id"]) + str(id) + '" required/>'
            html += '<label for="' + str(id) + '">' + i + '</label>'
        html+="</p>"

#Type 2 code
    elif liste_question[id_q]["type"] == 2:
        html = """
            <form method="post">
            <div id="type2" class="container">
            <h2>
            """
        html += liste_question[id_q-1]["question"]
        html += """
                </h2>
                <p>
                <input type="text" name=
                """
        html += liste_question[id_q-1]["question"]
        html += """
            " placeholder="Answer..." required/>
            </p>
            </div>
            """
#Type 3 code
    elif liste_question[id_q]["type"] == 3:
        pass

    elif liste_question[id_q]["type"] == 4:

        html="""
            <form method="post" action="">
            <div id="type4" class="container">
            <h2>
            """
        html += liste_question[id_q-1]["question"]
        html += "</h2><p>"

        for i in liste_question[id_q-1]["answer"]:
            id = liste_question[id_q-1].index(i)
            html +='<input type="checkbox" name=' + i
            html += 'value=' + liste_question[id_q-1]["id"] + str(id)
            html += 'id="' + str(id) + '"/>'
            html += '<label for=' + str(id) + '>' + i + '</label>'
            html+="</p>"

#Code 5
    elif liste_question[id_q]["type"] == 5:

        question_list = liste_question[id_q-1]["question"]
        answer_list = liste_question[id_q-1]["column"]

        html = """
            <div id="type5" class="container">
            <h2>{That is the title}</h2>
            <table style="width:100%">
            """

        for i in question_list:
            html +="""
                <tr>
                <td><h2>
            """
            html += liste_question[id_q-1]["title"]
            html += "</h2></td>"
            for j in answer_list:
                html += """
                        <td>
                        <input type="radio"
                        name="
                        """
                html += int(liste_question[id_q-1]["id"] + i + 1)
                html += """
                        "
                        value = "
                        """
                html += int(liste_question[id_q-1]["id"] + i + 1) + ":" + answer_list[j] + '"'
                html += """
                        id="
                        """
                html += answer_list[j] + '"'
                html += """
                        />
                        <label for="
                        """
                html += answer_list[j] + '"'
                html += ">" + answer_list[j] + "</label></td>"
            html += "</tr>"
            html += "</table></div>"

 #Code type 6
    elif liste_question[id_q]["type"] == 6:
        question_list = liste_question[id_q-1]["question"]
        answer_list = liste_question[id_q-1]["column"]

        html = """
            <div id="type5" class="container">
            <h2>{That is the title}</h2>
            <table style="width:100%">
            """

        for i in question_list:
            html +="""
                <tr>
                <td><h2>
            """
            html += liste_question[id_q-1]["title"]
            html += "</h2></td>"
            for j in answer_list:
                html += """
                        <td>
                        <input type="checkbox"
                        name="
                        """
                html += int(liste_question[id_q-1]["id"] + i + 1)
                html += """
                        "
                        value = "
                        """
                html += int(liste_question[id_q-1]["id"] + i + 1) + ":" + answer_list[j] + '"'
                html += """
                        id="
                        """
                html += answer_list[j] + '"'
                html += """
                        />
                        <label for="
                        """
                html += answer_list[j] + '"'
                html += ">" + answer_list[j] + "</label></td>"
            html += "</tr>"
        html += "</table></div>"


    elif liste_question[id_q]["type"] == 7:
        pass

#Type 8
    elif liste_question[id_q]["type"] == 8:
        answer_list = liste_question[id_q-1]["answer"]
        html = """
            <div id="type8" class="container">
            <h2>
            """
        html += liste_question[id_q-1]["question"]
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


def parcours_q(id_debut):
    html = display_intro_header()
    for i in range(id_debut, 87):
        if not i in liste_choix_deter:
            html += print_q(i+1, html)
        else:
            break
    print(html+display_out_footer())

def recup_valeurs():
	form = cgi.FieldStorage()
	if form:
		idx = 0
		for i in form:
			if not form[i].value == "next":
				idx +=1
		print(idx-1)

		radio = form.getvalue("")
	else:
		print('')

############
#MAIN
#############

recup_valeurs()
parcours_q(goto(0,""))
