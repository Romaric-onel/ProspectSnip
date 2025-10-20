from utils import clear_terminal
clear_terminal()
print("""Bienvenue sur ProspectSnip, un outil développé par Romaric pour trouver des enteprises en France.
Pour fermer l'outil, saisissez juste 'exit' à n'importe quelle entrée
""")
from GouvDataFr.use_api import main

main()