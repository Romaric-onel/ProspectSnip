import time
A1 = time.time()
from GouvDataFr.work_api_result import resultat_to_sheet
from utils import clear_terminal, print_animate_texte, create_log_file


MESSAGE_BIENVENUE = "Bienvenue sur ProspectSnip, un outil développé par Romaric Onel Hounsinou"
MESSAGE_FONCTIONNALITE = "Trouver des cibles et automatiser les mails personnalisés en un seul endroit"

clear_terminal(0)
print_animate_texte(MESSAGE_BIENVENUE, attributs=["bold", "blink"], duree=5)
for _ in range(2): print()
print_animate_texte(MESSAGE_FONCTIONNALITE, attributs=["bold", "blink"])

log_file = create_log_file()

if __name__ == "__main__":
    resultat_to_sheet()
A2 = time.time()

for _ in range(4): print()

print(f"Le temps total est de {A2-A1}")
