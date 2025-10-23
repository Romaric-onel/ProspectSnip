from utils import clear_terminal
from GouvDataFr.work_api_result import resultat_to_sheet
from utils import create_log_file
clear_terminal(0.01)
print("""Bienvenue sur ProspectSnip, un outil développé par Romaric pour trouver des enteprises en France.
Pour fermer l'outil, saisissez juste 'exit' à n'importe quelle entrée
""")
clear_terminal(2)
log_file = create_log_file()

if __name__ == "__main__":
    resultat_to_sheet()