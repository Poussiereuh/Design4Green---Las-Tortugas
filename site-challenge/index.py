from fonctions import fonctions


Single choice = {
    "question": "",
    "type": 1,
    "answer": ["ok", "boloss"]
    }

Text field = {
    "question": "",
    "type": 2,
    "answer": "text"
    }

Single choice + text field = {
    "question": "",
    "type": 3,
    "answer": ["ok", "boloss", "text"]
    }

QCM = {
    "question": "",
    "type": 4,
    "answer": ["ok", "boloss"]
    }

Tableau = {
	"question" : "",
	"type" : 5,
	"answer" : [],
	"column" : ["Used", "Not used functional", "Neither used nor functional"]
]

	}


q1 = {
	"id" : 1;
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
	"answer" : [
				"I don't know",
				"I do not want to answer"
				"m²"
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
	"question" : "Do you know the PUE of your Data Center? (PUE : Power Usage Effectiveness)",
	"type" : 1,
	"answer" : [
				"Less than 1,6",
				"Between 1,6 and 2,1",
				"More than 2,1",
				"I don't know"
				]
	}





LOUIS TU CASSES LES COUILLES



q86 = {
	"id" : 86;
	"question" : "Do you prefer the use of recycled paper?",
	"type" : 4,
	"answer" : [
				"Yes, our paper is made from virgin paste",
				"Yes, mixed paper",
				"Yes, 100\% recycled",
                "Yes, European Label",
                "I'm not paying attention",
                "Yes, other", // >> comment fields to add"
				]
	}

q87 = {
	"id" : 87;
	"question" : "Do you choose certified paper?",
	"type" : 7,
	"answer" : [
				"Yes, FSC",
				"Yes, PEFC",
				"Yes, Blue Angel",
                "Yes, European Label",
                "I'm not paying attention",
                "Yes, other", // >> comment fields to add"
				]
	}

q88 = {
	"id" : 88;
	"question" : "Do you organize the separate collection of waste paper for recycling?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know",
				]
	}


print(dictionnaire["answer"][0])
