from utils import clear_terminal
from GouvDataFr.use_api import combine_all_result
import asyncio
clear_terminal(0.01)
print("""Bienvenue sur ProspectSnip, un outil développé par Romaric pour trouver des enteprises en France.
Pour fermer l'outil, saisissez juste 'exit' à n'importe quelle entrée
""")
clear_terminal(2)


if __name__ == "__main__":
    asyncio.run(combine_all_result())