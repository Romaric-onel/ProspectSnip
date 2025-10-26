import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Callable

from decouple import config
from loguru import logger

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
        if not choice_int in range(1, len(LIST_CHOICES) + 1):
            print(f"\nVeuillez entre un chiffre entre 1 et {len(LIST_CHOICES)}")
            return function()

        choice = LIST_CHOICES[choice_int - 1]

        return choice

    elif verif is False:
        return function()


def clear_terminal(n: float | int):
    time.sleep(n)
    if os.name == "nt":  # windows
        os.system("cls")

    else:  # macos et linux
        os.system("cls")


def create_log_file():
    logs = Path("logs")
    logs.mkdir(exist_ok=True)

    logger.remove()
    logger.add(
        sys.stderr,
        level="ERROR",
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - {message}",
        backtrace=True,  # True si tu veux backtrace complet (plus verbeux)
        diagnose=False,  # True pour plus de détails (lent)
    )

    logger.add(
        logs / "ProspectSnip.log",
        level="DEBUG",
        rotation="10 MB",
        retention="14 days",
        compression="zip",
        enqueue=True,  # safe pour multithreading / multiprocessing
    )
