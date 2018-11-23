P=''
n='Yes, European Label'
m='</h2>'
X='How many virtual servers do you have?'
V='Next'
G="I don't know"
I=':'
p='</h2>\n\t'
D='column'
N=' '
E='answer'
M='textfield'
d='In quantity'
Q='</div>'
g='Start!'
L='Used'
R='I do not want to answer'
F='No'
A='id'
Z="'])"
b="I'm not paying attention"
_='[]"\n\t\t\t\t\t\t   value=" '
a='<input onclick="setFocus(\' '
O=' ">'
l="',])"
o=' \')" id=" '
Y='In %'
e='Do you use a modular application architecture?'
J='Not used functional'
U='text'
S='</label>'
W='</p>'
K='Neither used nor functional'
H='Yes'
h='intro'
c='Have you led or are you planning actions to optimize your infrastructure? Especially :'
B='question'
T=' "\n\t\t\t\t\t\t   id=" '
q='I do not know'
k=' :textfill" type="text" name="other"/>'
f='\n\t\t\t<p>\n\t\t\t\t<input onclick="resetTxtField(['
C='type'
from cgi import FieldStorage
from random import randrange
form=FieldStorage()
q0={A:0}
q1={A:1,B:'In which sector of activity is your company active? (linked with your APE code)',C:1,E:['Industry','Business','Information and communication','Other services activity','All other activities (financial, agricultural activities ...)','Construction','Public sector','Specialized','Scientific and Technical or Administrative and Support Services Activities','Real estate']}
q2={A:2,B:'What is the number of employees in your company on 18/12/31?',C:1,E:['0','1 to 2','3 to 9','10 to 49','50 to 249','250 to 4999','More than 5000']}
q3={A:3,B:'What is the turnover of your company in the last fiscal year? (or annual budget for Public sector)',C:1,E:['0 to 100K€','100 to 500 K€','500 to 2 M€','2 to 10 M€','10 to 50 M€','More than 50 M€']}
q4={A:4,B:'Do you develop digital services for internal or external use (sales to customers)?',C:1,E:[H,F]}
q5={A:5,B:'What is the number of users of your digital services?',C:2,E:U}
q6={A:6,C:5,B:'Do you apply the rules and best practices for digital accessibility?',D:[H,F,G]}
q7={A:7,C:5,B:'Have you optimized the states and printouts in your application tools (reduced number of pages when printing, ink consumption ...)?',D:[H,F,G]}
q8={A:8,C:5,B:'Do you integrate the principles of the ecodesign of digital services?',D:[H,F,G]}
q9={A:9,C:5,B:e,D:[H,F,G]}
q10={A:10,C:5,B:e,D:[H,F,G]}
q11={A:11,B:'What is the overall storage volume of your corporate data (centralized on external hard drives, centralized server, NAS, SAN ...) in Terabytes (TB) useful?',C:3,M:[2],E:[G,R,'TB']}
q12={A:12,B:'Do you have a server or do you only work with one or more workstations?',C:1,E:['We work with workstation(s), without centralized physical server','We have (at least) a centralized physical server']}
q13={A:13,B:'Do you have a dedicated room, simple room or cupboard with bay dedicated to your IT infrastructure?',C:1,E:['A closet or a room without any specific system','A dedicated room']}
q14={A:14,B:'Is your computer room in house or at a host?',C:1,E:['Internal','Host Member of the European Code of Conduct for Datacenters','Non-adhering Host of the European Code of Conduct for Data Centers']}
q15={A:15,B:'What is the total area of your computer rooms (excluding technical infrastructure *)? (in m2)',C:3,M:[0],E:["m²I don't know",R]}
q16={A:16,B:'Do you know the PUE of your Data Center? (PUE : Power Usage Effectiveness)',C:1,E:['Less than 1,6','Between 1,6 and 2,1','More than 2,1',G]}
q17={A:17,B:'What is the rate of charge or energy use of your computer rooms? (Rate = Electrical power absorbed by your IT equipment, divided by room capacity in kW, then multiplied by 100 (used energy / available energy))',C:1,E:['100% - 90%','90% - 60%','Less than 60%',G]}
q18={A:18,C:5,B:c,D:[H,F,G]}
q19={A:19,C:5,B:'The purchase of non-IT equipment from IT rooms (air conditioning, air treatment, inverters, etc.) according to energy efficiency criteria',D:[H,F,G]}
q20={A:20,C:5,B:'Implementing the good practices of the "European Code of Conduct for DataCenter?" ',D:[H,F,G]}
q21={A:21,C:5,B:'Data center PUE tracking',D:[H,F,G]}
q22={A:22,C:5,B:'Regular monitoring of environmental indicators of computer rooms',D:[H,F,G]}
q23={A:23,C:5,B:'Environmental impact analysis of the datacenter in life cycle approach',D:[H,F,G]}
q24={A:24,C:5,B:'Optimizing the architecture and layout of rooms',D:[H,F,G]}
q25={A:25,C:5,B:'The urbanization of halls in hot / cold aisles',D:[H,F,G]}
q26={A:26,C:5,B:'Containment of air flows (corridors)',D:[H,F,G]}
q27={A:27,C:5,B:'The use of natural cooling sources (freecooling)',D:[H,F,G]}
q28={A:28,C:5,B:'Implementation of a heat recovery system for computer rooms (heating)',D:[H,F,G]}
q29={A:29,C:5,B:'The set temperature in the cold corridor remains higher than 24 °',D:[H,F,G]}
q30={A:30,C:5,B:'The choice of a modular datacenter architecture',D:[H,F,G]}
q31={A:31,C:5,B:c,D:[H,F,G]}
q32={A:32,C:5,B:'Suspending network equipment',D:[H,F,G]}
q33={A:33,C:5,B:'Pooling physical equipment',D:[H,F,G]}
q34={A:34,C:5,B:'Uninstalling unnecessary infrastructure',D:[H,F,G]}
q35={A:35,C:5,B:'Traceability of material elements (CMDB)',D:[H,F,G]}
q36={A:36,C:5,B:'The correct sizing of the servers in relation to their use',D:[H,F,G]}
q37={A:37,C:5,B:'Give priority to ASHRAE 2 compatible equipment',D:[H,F,G]}
q38={A:38,C:5,B:'A procedure for provisioning and de-provisioning data-processing equipment in datacenters',D:[H,F,G]}
q39={A:39,B:'Do you know the number of physical servers and virtual servers in your company?',C:1,E:[F,R,H]}
q40={A:40,B:'How many physical servers do you have?',C:2,E:U}
q41={A:41,B:X,C:2,E:U}
q42={A:42,B:X,C:3,M:[0,1],E:[Y,d,R,G]}
q43={A:43,B:'What will be the evolution of your number of virtual servers for 2019? (in% or quantity)',C:3,M:[0,1],E:[Y,d,"I do not want to answerI don't know"]}
q44={A:44,B:'Has your company appointed a Green IT Manager / Digital Manager?',C:1,E:[H,F,G]}
q45={A:45,B:'Do you have a responsible digital strategy broken down into an action plan?',C:1,E:[H,F,G]}
q46={A:46,B:'Is Green IT a topic integrated into your CSR strategy?',C:1,E:[H,F,G]}
q47={A:47,B:'Do you regularly evaluate the environmental impacts of your information system?',C:1,E:['Yes partially, including only equipment present in the company','Yes totally, including our internal equipment and services hosted by third parties',F,q]}
q48={A:48,B:'Do you have a team of competent referees on the topics of Green IT?',C:1,E:[H,F,G]}
q49={A:49,B:'Have you integrated Green IT into your business strategy',C:1,E:[H,F,G]}
q50={A:50,C:5,B:'Do you have those equipments in your compagny: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)',D:[L,J,K]}
q51={A:51,C:5,B:'Fixed stations, workstations',D:[L,J,K]}
q52={A:52,C:5,B:'Laptops, digital tablets',D:[L,J,K]}
q53={A:53,C:5,B:'Small printers (<15kg, potentially used by a household)',D:[L,J,K]}
q54={A:54,C:5,B:'Flat screen monitors',D:[L,J,K]}
q55={A:55,C:5,B:'Other flat screens (TV, projection screen, digital board ...)',D:[L,J,K]}
q56={A:56,C:5,B:'CRT monitors (monitors or other)',D:[L,J,K]}
q57={A:57,C:5,B:'Video projectors',D:[L,J,K]}
q58={A:58,C:5,B:'Mobile phones',D:[L,J,K]}
q59={A:59,C:5,B:'Fixed telephones (standalone not connected to such a standard)',D:[L,J,K]}
q60={A:60,C:5,B:'Digital cameras',D:[L,J,K]}
q61={A:61,C:5,B:'Hard Disk Devices, Storage, Backup',D:[L,J,K]}
q62={A:62,B:'Do you have other devices in your company? (Keyboards, mouse, graphic tablets, scanners, microphones, speakers, office equipment ...)',C:1,E:[H,F]}
q63={A:63,C:5,B:'Regarding other devices, do you have in your company: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)',D:[L,J,K]}
q64={A:64,C:5,B:'Keyboards',D:[L,J,K]}
q65={A:65,C:5,B:'Mouse',D:[L,J,K]}
q66={A:66,C:5,B:'Graphic Tablets',D:[L,J,K]}
q67={A:67,C:5,B:'Scanners',D:[L,J,K]}
q68={A:68,C:5,B:'Speakers',D:[L,J,K]}
q69={A:69,C:5,B:'Office Automation',D:[L,J,K]}
q70={A:70,B:'Do you know the consumption of your workstation in kWh per year?',C:3,M:[0],E:['Yes (please specify how much in kWh / year)',F]}
q71={A:71,B:'Do you track the energy consumption of your compagny activities?',C:1,E:[H,F,G]}
q72={A:72,B:"Do you know the share of IT and IT equipment in your company's total energy consumption?",C:3,M:[0],E:['Yes (please specify how much in %)',F]}
q73={A:73,B:'Have you set up a power management system? (automatic shutdown / shutdown of workstations)',C:1,E:[H,F,G]}
q74={A:74,B:'Do you use copiers from a repackaging industry (second-hand / second-hand)?',C:1,E:[H,F,G]}
q75={A:75,B:'Do you consolidate individual printers to shared printers?',C:1,E:[H,F,G]}
q76={A:76,B:'Have you set up an identification system on printers (to trigger printing)?',C:1,E:[H,F,G]}
q77={A:77,B:'What is the average life of your professional copier / MFP *? * MFP Multi Fonction Printer',C:3,M:[2],E:[q,'Do not want to answer','x years (please specify)']}
q78={A:78,C:5,B:'Are your printers set by default in eco mode? Especially :',D:[H,F,G]}
q79={A:79,C:5,B:'Energy saving (Automatic standby)',D:[H,F,G]}
q80={A:80,C:5,B:'Black and white by default',D:[H,F,G]}
q81={A:81,C:5,B:'Default duplex',D:[H,F,G]}
q82={A:82,C:5,B:'Default draft mode',D:[H,F,G]}
q83={A:83,B:'What is the number of pages printed / day / employee? (A4 equivalent)',C:1,E:['Less than 10','From 10 to 20','From 20 to 30','More than 30',G]}
q84={A:84,B:'Can you specify the number of cartridges / toners:',C:8,E:['Cartridges used a year','Cartridges stored in the average business','Toners used a year','Toners stored in the average business']}
q85={A:85,B:'Do you organize the separate collection of waste cartridges / toners?',C:1,E:['Yes, to a repackaging industry','Yes, towards a recycling channel (destruction)','No no separate collection device is planned']}
q86={A:86,B:'Do you prefer the use of recycled paper?',C:4,E:['Yes, our paper is made from virgin paste','Yes, mixed paper','Yes, 100\\% recycled',n,b]}
q87={A:87,B:'Do you choose certified paper?',C:7,M:[4],E:['Yes, FSC','Yes, PEFC','Yes, Blue Angel',n,'Yes, other',b]}
q88={A:88,B:'Do you organize the separate collection of waste paper for recycling?',C:1,E:[H,F,G]}
liste_question=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88]
def display_intro_header():return'<!DOCTYPE html>\n\t<html lang="fr">\n\t<head>\n\t\t<title>Las tortugas: Online SURVEY</title>\n\t\t<meta charset="utf-8" />\n\t\t<meta name="description" content="text/html;" />\n\t\t<link rel="icon" href="favicon.ico"/>\n\t\t<link rel="stylesheet" type="text/css" href="style.css">\n\t</head>\n\t<body>\n\t\t<form method="post" action="">\n\t\t<div id="type1" class="container">\n\t'
def display_intro_msg():return'\n\t<h1>Las TORTUGAS SURVEY</h1>\n\t<p>Welcome to the online survey of TORTUGAS SURVEY team</p>\n\t<p> The main goal of this server is to gather your opinion on the subject XXX</p>\n\t<form action="" method="post">\n\t\t\t<input type="text" name="email" value="" />\n\t\t\t<input type="submit" name="send" value="Rechercher">\n\t</form>\n\t'
def display_out_footer():return'<input type="submit" name="next" value="Next"/></div></form></body><footer></footer></html>'
def type1(id_q):
	html='\n\t<div id="type1" class="container">\n\t\t<h2>%s %s</h2>'%(str(liste_question[id_q-1][A]),liste_question[id_q-1][B])
	for i in liste_question[id_q-1][E]:html+='\n\t\t<p>\n\t\t\t<input type="radio"\n\t\t\t\t\tname=" '+str(liste_question[id_q-1][A])+' "\n\t\t\t\t\tvalue=" '+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+' "\n\t\t\t\t\tid=" '+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+' " required/>\n\n\t\t\t<label for=" '+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+O+i+'</label>\n\t\t</p>'
	html+=Q;return html
def type2(id_q):return'\n\t<div id="type2" class="container">\n\t<h2>'+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+'</h2>\n\t\t<p>\n\t\t\t<input type="text"\n\t\t\t\t   name=" '+str(liste_question[id_q-1][A])+' "\n\t\t\t\t   id=" '+str(liste_question[id_q-1][A])+':0"\n\t\t\t\t   placeholder="Answer..." required/>\n\t\t</p>\n\t</div>\n\t'
def type3(id_q):
	answer_list=liste_question[id_q-1][E];text_answer=liste_question[id_q-1][M];resetTxtField=P
	for machin in text_answer:resetTxtField+="' "+str(liste_question[id_q-1][A])+I+str(machin)+" ',"
	html='\n\t<div id="type3" class="container">\n\t\t<h2>'+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+m
	for i in answer_list:
		html+=f+resetTxtField+'])"\n\t\t\t\t\t   type="radio"\n\t\t\t\t\t   name=" '+str(liste_question[id_q-1][A])+' "\n\t\t\t\t\t   value=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+' "\n\t\t\t\t\t   id=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+' " required/>\n\t\t\t\t<label for=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+O+i+S
		for pos in text_answer:
			if pos==answer_list.index(i):html+=a+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+o+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+k
		html+=W
	html=html.replace(l,Z);html+=Q;return html
def type4(id_q):
	html='\n\t<div id="type4" class="container">\n\t\t<h2>'+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+p
	for i in liste_question[id_q-1][E]:
		id=liste_question[id_q-1][A];html+='\n\t\t\t\t<p>\n\t\t\t\t\t<input type="checkbox"\n\t\t\t\t\t\t   name=" '+str(liste_question[id_q-1][A])+_+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+T+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+' "/>\n\t\t\t\t\t<label for=" '+str(liste_question[id_q-1][A])+I+str(liste_question[id_q-1][E].index(i))+O+i+'</label>\n\t\t\t\t</p>'
	html+=Q;return html
def type5(id_q):
	question_list=liste_question[id_q-1][B];answer_list=liste_question[id_q-1][D];html='\n\t<div id="type5" class="container">\n\t\t<table style="width:100%">\n\t\t\t <tr>\n\t\t\t   <td><h2> '+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+'</h2></td>'
	for j in answer_list:html+='\n\t\t\t\t   <td>\n\t\t\t\t\t   <input type="radio"\n\t\t\t\t\t\t  name=" '+str(liste_question[id_q-1][A])+' "\n\t\t\t\t\t\t  value=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(j))+' "\n\t\t\t\t\t\t  id=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(j))+' "/>\n\n\t\t\t\t\t   <label for=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(j))+O+j+'</label>\n\t\t\t\t   </td>'
	html+='</tr>\n\t</table>\n\t</div>';return html
def type6(id_q):
	question_list=liste_question[id_q-1][B];answer_list=liste_question[id_q-1][D];html='\n\t<div id="type6" class="container">\n\t\t<table style="width:100%">\n\t\t\t <tr>\n\t\t\t   <td><h2>'+str(liste_question[id_q-1]['title'])+'</h2></td>\n\t'
	for j in answer_list:
		html+='\n\t\t\t\t   <td>\n\t\t\t\t\t   <input type="checkbox"\n\t\t\t\t\t\t  name="\n\t\t';html+=str(liste_question[id_q-1][A])+' " ';html+='value=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(j))+' "id=" ';html+=str(answer_list.index(j))+' "/>';html+='<label for='+str(answer_list.index(j))+'">'+j+S;html+='</td>'
	html+='\n\t\t</tr>\n\t\t\t</table>\n\t\t</div>\n\t';return html
def type7(id_q):
	answer_list=liste_question[id_q-1][E];text_answer=liste_question[id_q-1][M];resetTxtField=P
	for machin in text_answer:resetTxtField+="'"+str(machin)+"',"
	html='\n\t<div id="type7" class="container">\n\t\t<h2>'+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+p
	for i in answer_list:
		html+=f+resetTxtField+'])"\n\t\t\t\t\t\t   type="checkbox"\n\t\t\t\t\t\t   name=" '+str(liste_question[id_q-1][A])+_+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+T+str(answer_list.index(i))+' "/>\n\n\t\t\t\t\t<label for=" '+str(answer_list.index(i))+O+i+S
		for pos in text_answer:
			if pos==answer_list.index(i):html+=a+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+o+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+k
		html+=W
	html=html.replace(l,Z);html+=Q;return html
def type8(id_q):
	answer_list=liste_question[id_q-1][E];html='\n\t<div id="type8" class="container">\n\t\t<h2>'+str(liste_question[id_q-1][A])+N+str(liste_question[id_q-1][B])+m
	for i in answer_list:html+='\n\t\t\t\t<p>\n\t\t\t\t\t<label for=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+O+i+'</label>\n\t\t\t\t\t<input type="number"\n\t\t\t\t\t\t   name=" '+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+T+str(liste_question[id_q-1][A])+I+str(answer_list.index(i))+' "\n\t\t\t\t\t\t   placeholder=" '+i+' " required/>\n\t\t\t\t</p>'
	html+=Q;return html
def header():return'<!DOCTYPE html>\n\t<html lang="fr">\n\n\t<head>\n\t\t<title>Las tortugas - </title>\n\t\t<meta charset="utf-8"  />\n\t\t<link rel="icon" type="image/png" href="/img/favicon.png"/>\n\t\t<meta name="description" content="" />\n\t\t<link rel="stylesheet" type="text/css" href="style.css">\n\t</head>\n\n\t<body>\n\t\t<div class="head"></div>\n\t\t<div class="mainContainer">\n\t'
def intro():return'\n\t<div class="container justify">\n\t\t<h2>Welcome to the Design4Green survey!</h2>\n\t\t<p>\n\t\t\tWith the support of ADEME, the Ministry of Ecology, Energy and the Sea and the\n\t\t\tMinistry of Economy and Finance, the association AGIT (Alliance for Green IT) and\n\t\t\tthe eco-organizations of the recycling network of Waste Electrical and Electronic\n\t\t\tEquipment (WEEE) organize a survey to assess the deposits of computer and office\n\t\t\tequipment present in companies and more generally on the maturity of companies in\n\t\t\tFrance in the use of eco-responsible digital services.\n\t\t</p>\n\t\t<p>\n\t\t\tThe duration of the questionnaire is estimated at 15 minutes if you are able to\n\t\t\tanswer questions directly.\n\t\t</p>\n\t\t<p>\n\t\t\tYou can return at any time on the questionnaire, answer in several times, your\n\t\t\tprevious answers are recorded. In case of modification, only the last answer will\n\t\t\tbe taken into account.\n\t\t</p>\n\t\t<p>\n\t\t\tYou can submit this questionnaire to several people in your organization. All you\n\t\t\thave to do is simply share the link to the questionnaire.\n\t\t</p>\n\t\t<p>\n\t\t\tThank you for participating in this survey. Your answer is invaluable to us to\n\t\t\tconstitute the most representative sample of the companies in France.\n\t\t</p>\n\t\t<form method="post" action="">\n\t\t\t<input name="email" type="email" placeholder="Email" required/>\n\t\t\t<input class="button" name="intro" type="submit" value="Start!"/>\n\t\t</form>\n\t</div>\n\t'
def startform():return'<form method="post" action=""><input type="hidden" name="save_email" value=\''+variable_get+"'"
def footer(id):
	html=P
	if id==None:0
	elif id!=None:html='\n\t\t\t\t\t<input class="submit" type="submit" name="submit" value="Continue later"/>\n\t\t\t\t\t<input class="button" type="submit" name="next" value="Next"/>\n\t\t\t\t\t</form>\n\t\t\t\t   '
	elif id==89:html='\n\t\t\t<div class="container">\n\t\t\t\t<h2>Thank you!</h2>\n\t\t\t\t<p>Thank you for your answers. Now, you can download your report.</p>\n\t\t\t</div>\n\t\t</div>'
	html+='<script type="text/javascript" src="javascript.js"></script>\n\t</body>\n\t</html>\n\t';return html
def afficherFin():
	html='<div class="container">\n\t\t<h2>Thank you!</h2>\n\t\t<p>Thank you for your answers. Now, you can download your report.</p>\n\t</div>\n</div>';print(html)
def goto(id_q,id_rep):
	if id_q==4 and id_rep==0:return 5
	elif id_q==4 and id_rep==1:return 12
	elif id_q==12 and id_rep==0:return 50
	elif id_q==12 and id_rep==1:return 13
	elif id_q==13 and id_rep==0:return 31
	elif id_q==13 and id_rep==1:return 14
	elif id_q==39 and(id_rep==0 or id_rep==1):return 42
	elif id_q==39 and id_rep==2:return 40
	elif id_q==62 and id_rep==0:return 63
	elif id_q==62 and id_rep==1:return 70
def print_q(id_question,html):
	if liste_question[id_question-1][C]==0:html=intro()
	elif liste_question[id_question-1][C]==1:html=type1(id_question)
	elif liste_question[id_question-1][C]==2:html=type2(id_question)
	elif liste_question[id_question-1][C]==3:html=type3(id_question)
	elif liste_question[id_question-1][C]==4:html=type4(id_question)
	elif liste_question[id_question-1][C]==5:html=type5(id_question)
	elif liste_question[id_question-1][C]==6:html=type6(id_question)
	elif liste_question[id_question-1][C]==7:html=type7(id_question)
	elif liste_question[id_question-1][C]==8:html=type8(id_question)
	return html
def parcours_q(id_debut):
	liste_choix_deter=[4,12,13,39,62];html=P+header()+startform()
	if id_debut!=89:
		try:
			for qCourante in range(id_debut,len(liste_question)+1):
				html+=str(print_q(qCourante,html))
				if qCourante in liste_choix_deter:break
		except:afficherFin()
	html+=footer(id_debut);return html
def recup_valeurs():
	liste_tempo_csv=[];id_rand=str(randrange(0x9184e72a000,99999999999999))
	if form:
		if form.getvalue(h)==g:html=parcours_q(1)
		else:
			for i in form:
				try:
					if V not in form[i].value.split(I)[0]:
						question=form[i].value.split(I)[0]
						try:reponse=form[i].value.split(I)[1]
						except IndexError:pass
						liste_tempo_csv.append(str(question)+I+str(reponse))
				except AttributeError:pass
			liste_tempo_csv.sort();liste_tempo_csv.insert(0,id_rand);id_last_question=liste_tempo_csv[len(liste_tempo_csv)-1].split(I)[0];id_last_response=liste_tempo_csv[len(liste_tempo_csv)-1].split(I)[1];valeur=int(id_last_question);mareponse=int(id_last_response);return parcours_q(goto(valeur,mareponse))
	else:return P
html=recup_valeurs()
if form.getvalue(h)==g:html=parcours_q(1)
elif form.getvalue('next')!=V:html=header()+intro()
print(html)

