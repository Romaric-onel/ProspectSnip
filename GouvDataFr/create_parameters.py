from . import HEADERS, clear_terminal, navigate_location, return_entry


def ask_scrap_information() -> dict[str, str]:
    info = {}

    info["categorie_entreprise"] = ask_category()
    clear_terminal()
    info["territory"] = department_or_commune()

    if len(info["territory"][0]) > 3:
        info["departement"] = (", ".join(info.pop("territory"))).replace(" ", "")
    else:
        info["code_commune"] = (", ".join(info.pop("territory"))).replace(" ", "")
    info["est_entrepreneur_individuel"] = is_solopreneur()
    print(info)
    return info


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


def department_or_commune() -> str | list[str]:

    LIST_CHOICES = [
        (True, "Un Département français précis"),
        (False, "Une Région française précise"),
        (None, "Pas de préférences"),
    ]

    print("Vous aviez le choix. Que ciblez vous")
    for num, choice in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choice[1]}")

    choice: tuple = return_entry(ask_category, LIST_CHOICES)
    print(choice[0])
    if choice[0] == None:
        pass
    elif choice[0] == True:
        return choice_department()

    elif choice[0] == False:
        return choice_commune()


def choice_department() -> str | list[str]:
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


def choice_commune() -> str | list[str]:
    communes = []
    communes.append(navigate_location(True))
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
        (None, "Pas de préférence")
    ]
    for num, choice in enumerate(LIST_CHOICES):
        print(f"{num+1} - {choice[1]}")
    choice = return_entry(is_solopreneur, LIST_CHOICES)
    return choice[0]