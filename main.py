from utils import clear_terminal
clear_terminal()
print("""Bienvenue sur ProspectSnip, un outil développé par Romaric pour trouver des enteprises en France.
Pour fermer l'outil, saisissez juste 'exit' à n'importe quelle entrée
""")
from GouvDataFr.create_parameters import  ask_scrap_information
cat = ask_scrap_information()