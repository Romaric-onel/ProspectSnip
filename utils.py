import json
import os
import time
from typing import Any, Callable

import pandas as pd
from decouple import config
from tabulate import tabulate

DEPARTMENT_FILE = os.path.join(
    os.getcwdb().decode("utf-8"), "sources", "departement_fr_2025.csv"
)
COMMUNE_FILE = os.path.join(
    os.getcwdb().decode("utf-8"), "sources", "commune_fr_2025.csv.csv"
)
HEADERS = config("HEADERS", cast=lambda x: json.loads(x), default={})


def exit_fonction() -> None:
    print(
        """Merci d'avoir utilisé ProspectSnip.
N'hésitez pas à faire un retour à Hounsinou Romaric Onel sur LinkedIn"""
    )
    time.sleep(2)
    exit(0)


def entry_empty(entry: str) -> bool:
    if not entry:
        print(
            "Vous n'avez rien entré. Saisissez l'information demandée ou 'exit' pour sortir\n\n"
        )
        return False
    else:
        return True


def verify_entry() -> bool | int | None:
    choice_str = input(
        "\nVeuillez entrer le chiffre correspondant à votre demande ou 'exit' pour sortir : "
    )

    if choice_str == "exit":
        exit_fonction()
    if not entry_empty(choice_str):  # True quand on écrit et False quand rien est écrit
        return None
    try:
        choice_int = int(choice_str)
    except ValueError:
        print(
            "\nVeuillez saisir un chiffre sans espacement et sans caractères spéciaux\n"
        )
        return False
    return choice_int


def return_entry(function: Callable, LIST_CHOICES: list) -> Any:
    verif = verify_entry()
    if verif is None:
        return function()
    elif verif:
        choice_int = verif
        if not choice_int in range(1, len(LIST_CHOICES)+1):
            print(f"\nVeuillez entre un chiffre entre 1 et {len(LIST_CHOICES)}")
            return function()

        choice = LIST_CHOICES[choice_int - 1]

        return choice

    elif verif is False:
        return function()


def clear_terminal(n:float | int):
    time.sleep(n)
    if os.name == "nt":  # windows
        os.system("cls")

    else:  # macos et linux
        os.system("cls")


def navigate_location(loc: bool) -> int:
    if loc == True:
        filename = DEPARTMENT_FILE
        order = "REG"
        ch = "Département"
        name: list = [1, 5]
        step = 10
    else:
        filename = COMMUNE_FILE
        order = "COM"
        ch = "Commune"
        name: list = [9]
        step = 15
    data: pd.DataFrame = pd.read_csv(filename).sort_values(by=order, ascending=True)
    choice = 0

    i = 0
    print("---Bienvenue dans le menu de navigation---")
    print(
        "---Pour aller la page suivante, cliquez sur 'S' et 'P' pour la page précédente---"
    )
    while 0 <= i <= len(data):
        print(
            f"--L'objectif dans ce menu est de choisir le numéro de votre {ch} cible.\nAssurez vous qu'il est sur la page visible"
        )
        print()
        print(
            tabulate(
                data.iloc[i : i + step, name],  # type: ignore
                headers=["Num", ch],
                tablefmt="github",
                showindex=True if not loc else False,
            )
        )
        print(f"\n--- Affiché {i} à {min(i+step, len(data))} sur {len(data)} ---\n")
        cmd = input("Saisissez une commande ... ")
        if cmd.upper() == "S":
            if i == len(data) - step:
                print("Vous êtes déjà à la dernière page")
                return navigate_location(loc)
            else:
                i += step
        elif cmd.upper() == "P":
            if i == 0:
                print("Vous êtes à la première page de navigation")
                return navigate_location(loc)
            else:
                i -= step
        elif not entry_empty(cmd):
            print(
                "Vous avez entré une commande vide.\nRetour au début du menu de navigation"
            )
        else:

            try:
                choice_num = int(cmd)

            except ValueError:
                print("Commande non reconnue")
                return navigate_location(loc)
            else:
                if not i in range(i, i + step):
                    print(
                        "Vous ne pouvez entrer que les numéros de {ch} présents sur cette page.\nVous pouvez appuyer sur 'S' pour la page suivante ou 'P' pour la page précédente"
                    )
                break

    if loc:
        choice = data.loc[choice_num - 1, "DEP"]
    else:
        choice = data.loc[choice_num, "COM"]

    print(f"Excellent !!! Vous avez ajouté le {ch} {choice} à votre ciblage")
    return choice


