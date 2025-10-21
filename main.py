from utils import clear_terminal
clear_terminal(0.01)
print("""Bienvenue sur ProspectSnip, un outil développé par Romaric pour trouver des enteprises en France.
Pour fermer l'outil, saisissez juste 'exit' à n'importe quelle entrée
""")
clear_terminal(2)
from GouvDataFr.use_api import combine_all_result

if __name__ == "__main__":
    combine_all_result()