from . import (
    HEADERS,
    clear_terminal,
    entry_empty,
    exit_fonction,
    os,
    pd,
    return_entry,
    verify_entry,
)




def ask_scrap_information() -> dict[str, str]:
    info = {}

    info["category"] = ask_category()
    clear_terminal()
    info["territory"] = department_or_commune()

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


def department_or_commune() -> str:

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


def choice_department() -> str:
    
    print("Vous êtes libre de choisir entre un seul ou plusieurs départements")
    print(
        """
1- Je cible un seul département
2- Je cible plusieurs départements
"""
    )
    choice: int = return_entry(choice_department, ["1", "2"])
    print("Le choix est", choice)
    if choice == 1:
        print(
            """Vous avez décidé de choisir un seul département.\nNous vous les présenterons par lot de 10.\nPour aller sur la page suivante, cliquez sur la lettre S, P pour le précédent.\nL'objectif est de choisir le numéro de votre ville"""
        )
        
    


def choice_commune() -> str:
    name = ""
    return name
