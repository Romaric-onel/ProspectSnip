from . import clear_terminal, navigate_location, return_entry

INFOS = {}
INFOS["per_page"] = 25
INFOS["page"] = 1
def ask_scrap_information() -> dict[str, str]:

    global INFOS
    INFOS["categorie_entreprise"] = "GE"
    """INFOS["categorie_entreprise"] = ask_category()
    clear_terminal(1)
    
    INFOS["territory"] = department_or_commune()
    clear_terminal(1)
    if INFOS["territory"]:
        if len(INFOS["territory"][0]) <= 3:
            INFOS["departement"] = (", ".join(INFOS.pop("territory"))).replace(" ", "")
        else:
            INFOS["code_commune"] = (", ".join(INFOS.pop("territory"))).replace(" ", "")
    clear_terminal(1)
    INFOS["est_entrepreneur_individuel"] = is_solopreneur()
    clear_terminal(1)
    INFOS["est_organisme_formation"] = est_organisme_formation()
    clear_terminal(1)
    INFOS["tranche_effectif_salarie"] = tranche_effectif_salarie()
    clear_terminal(1)
    info_connaissance()
    clear_terminal(1)
    chiffre_affaires()
    clear_terminal(1)
    resultat_net()
    clear_terminal(1)"""
    print(INFOS)
    INFOS = {key: value for key, value in INFOS.items() if value is not None}
    return INFOS


def ask_category() -> str:
    LIST_CHOICES = [
        ("PME", "Petites et moyennes entreprises"),
        ("ETI", "Entreprises de taille intermédiaire"),
        ("GE", "Grandes entreprises"),
    ]

    print("Voici les catégories disponibles en France\n")

    for num, category in enumerate(LIST_CHOICES):
        print(f"{num+1} - {category[1]}")

    choice: tuple = return_entry(ask_category, LIST_CHOICES)
    print(f"Excellent choix ! Vous aviez choisi '{choice[1].upper()}'")
    return choice[0]


def department_or_commune():

    LIST_CHOICES = [
        (True, "Un Département français précis"),
        (False, "Une Commune française précise"),
        (None, "Pas de préférences"),
    ]

    print("Vous aviez le choix. Que ciblez vous")
    for num, choice in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choice[1]}")

    choice: tuple = return_entry(ask_category, LIST_CHOICES)

    if choice[0] == None:
        pass
    elif choice[0] == True:
        return choice_department()

    elif choice[0] == False:
        return choice_commune()


def choice_department():
    departments = []
    departments.append(navigate_location(True))
    retry = "Non"

    print("Souhaitez vous cibler un autre département ?\n1-Oui\n2-Non")
    retry = return_entry(choice_department, ["Oui", "Non"])
    while retry == "Oui":
        departments.append(navigate_location(True))
        print("Souhaitez vous cibler un autre département ?\n1-Oui\n2-Non")
        retry = return_entry(choice_department, ["Oui", "Non"])

    return list(dict.fromkeys(departments))


def choice_commune():
    communes = []
    communes.append(navigate_location(False))
    retry = "2"
    print("Souhaitez vous cibler une autre commune ?\n1-Oui\n2-Non")

    retry = return_entry(choice_department, ["Oui", "Non"])

    while retry == "Oui":

        communes.append(navigate_location(False))
        print("Souhaitez vous cibler une autre commune ?\n1-Oui\n2-Non")
        retry = return_entry(choice_department, ["Oui", "Non"])

    return list(dict.fromkeys(communes))


def is_solopreneur():
    LIST_CHOICES = [
        (True, "Est entrepreneur individuel"),
        (False, "N'est pas entrepreneur individuel"),
        (None, "Pas de préférence"),
    ]
    for num, choice in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choice[1]}")
    choice = return_entry(is_solopreneur, LIST_CHOICES)
    return choice[0]


def est_organisme_formation():
    LIST_CHOICES = [
        (True, "Je cible des organismes de formation"),
        (False, "Je ne cible pas des organismes de formation"),
        (None, "Je n'ai pas de préférences"),
    ]

    for num, choices in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choices[1]}")

    choice_num = return_entry(est_organisme_formation, LIST_CHOICES)
    choice = choice_num[0]

    return choice


def tranche_effectif_salarie():
    LIST_CHOICES = [
        ("NN", "Unité non-employeuse"),
        ("00", "0 salarié"),
        ("01", "1 ou 2 salariés"),
        ("02", "3 à 5 salariés"),
        ("03", "6 à 9 salariés"),
        ("11", "10 à 19 salariés"),
        ("12", "20 à 49 salariés"),
        ("21", "50 à 99 salariés"),
        ("22", "100 à 199 salariés"),
        ("31", "200 à 249 salariés"),
        ("32", "250 à 499 salariés"),
        ("41", "500 à 999 salariés"),
        ("42", "1 000 à 1 999 salariés"),
        ("51", "2 000 à 4 999 salariés"),
        ("52", "5 000 à 9 999 salariés"),
        ("53", "10 000 salariés et plus"),
    ]

    print("Veuillez choisir la tranche effectif salariale de votre cible")

    for num, choices in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choices[1]}")

    choice_num = return_entry(tranche_effectif_salarie, LIST_CHOICES)

    choice = choice_num[0]

    return choice


def info_connaissance():
    global INFOS
    print("Connaissez vous au moins une personne dans l'entreprise ?\n1-Oui\n2-Non")
    answer = return_entry(info_connaissance, ["Oui", "Non"])

    if answer == "Oui":
        INFOS["nom_personne"] = nom_personne()
        INFOS["prenoms_personne"] = prenoms_personne()
        if INFOS["nom_personne"] is not None or INFOS["prenoms_personne"] is not None:
            INFOS["type_personne"] = type_personne()


def nom_personne():
    nom = input(
        "Saisissez le nom de la personne.\nCliquez sur 'Entrer' pour passer ... "
    )
    if not nom:
        return None
    return nom


def prenoms_personne():
    prenom = input(
        "Entrez le(s) prénom(s) de la personne.\nCliquez sur 'Entrer' pour passer ... "
    )
    if not prenom:
        return None
    return prenom.split(" ")


def type_personne():
    print("Qu'est cette personne dans l'entreprise ?")

    LIST_CHOICES = [
        ("dirigeant", "Il s'agit d'un dirigeant"),
        ("elu", "Il s'agit d'un élu"),
        (None, "Ni l'un ni l'autre"),
    ]

    for num, choices in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choices[1]}")

    choice_num = return_entry(tranche_effectif_salarie, LIST_CHOICES)

    choice = choice_num[0]

    return choice


def chiffre_affaires():
    global INFOS
    print("Connaissez vous le chiffre d'affaires de votre cible ? \n\n1-Oui\n2-Non")

    answer = return_entry(chiffre_affaires, ["Oui", "Non"])

    if answer == "Oui":
        INFOS["ca_min"] = chiffre_affaires_min()
        INFOS["ca_max"] = chiffre_affaires_max()


def chiffre_affaires_min():
    ca_min_str = input(
        "Quelle est la valeur minimale du chiffre d'affaire de votre cible ? ... "
    )
    if not ca_min_str:
        return None
    try:
        ca_min = int(ca_min_str)
    except:
        print("Veuillez saisir un nombre sans virgule et sans caractères spéciaux")

        return chiffre_affaires_min()

    return ca_min


def chiffre_affaires_max():
    ca_max_str = input(
        "Quelle est la valeur maximale du chiffre d'affaire de votre cible ? "
    )
    answer = return_entry(chiffre_affaires, ["Oui", "Non"])

    if not ca_max_str:
        return None
    try:
        ca_max = int(ca_max_str)
    except:
        print("Veuillez saisir un nombre sans virgule et sans caractères spéciaux")

        return chiffre_affaires_max()

    return ca_max


def resultat_net():
    global INFOS
    print("Connaissez vous le resultat net de votre cible ?\n\n1-Oui\n2-Non")

    answer = return_entry(resultat_net, ["Oui", "Non"])

    if answer == "Oui":
        INFOS["resultat_net_min"] = resultat_net_min()
        INFOS["resultat_net_max"] = resultat_net_max()


def resultat_net_min():
    res_min_str = input(
        "Quel est le resultat net minimum de votre cible ?.\nCliquez sur 'Entrée' pour passer la question"
    )
    if not res_min_str:
        return None
    try:
        res_min = int(res_min_str)
    except:
        print("Veuillez saisir un nombre sans virgule et sans caractères spéciaux")

        return resultat_net_min()

    return res_min


def resultat_net_max():
    res_max_str = input(
        "Quel est le resultat net maximal de votre cible ?\nCliquez sur 'Entrée' pour passer la question"
    )
    if not res_max_str:
        return None
    try:
        res_max = int(res_max_str)
    except:
        print("Veuillez saisir un nombre sans virgule et sans caractères spéciaux")

        return resultat_net_max()

    return res_max
