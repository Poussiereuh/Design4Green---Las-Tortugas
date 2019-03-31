import json
while 1:
    with open('bdd.json', 'r', encoding="UTF-8") as f:
        datas = json.load(f)

    variable_get = input("email: ")
    #variable_get = form.getvalue("email")

    if datas[variable_get]:
        last_couple = datas[variable_get][len(datas[variable_get])-1]
        question_id = last_couple[0]

        if int(question_id) == 88:
            pass
        else:
            parcours_q(int(question_id))
    else:
        datas = {str(variable_get):[]}
        with open('bdd.json', 'w', encoding="UTF-8") as outfile:
            json.dump(datas, outfile, indent=4, ensure_ascii=False)

    # datas[variable_get] = {}
    #
    # #On renvoie la BDD modifiée avec le compteur
    # with open('bdd.json', 'w', encoding="UTF-8") as outfile:
    #     json.dump(datas, outfile, indent=4, ensure_ascii=False)
