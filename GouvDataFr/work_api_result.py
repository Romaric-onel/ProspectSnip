from openpyxl.workbook.workbook import Workbook

from . import asyncio, chain, json, openpyxl, os, pandas
from .use_api import combine_all_result


def resultat_to_sheet():
    raw_data = asyncio.run(combine_all_result())
    data = list(chain.from_iterable(item["results"] for item in raw_data))

    # création du fichier excel
    excel = openpyxl.Workbook()

    # création des feuilles sheet

    excel_presentation: Workbook = excel.active  # type: ignore
    excel_membre: Workbook = excel.create_sheet(title= "Membre")  # type: ignore
    excel_template = 
    #nom des feuilles créées
    excel_presentation.title = "Présentation"  # type: ignore
    

    #remplir les feuilles
    for i, cible in enumerate(data):
        
        excel_presentation.cell(row=i + 2, column=1, value=cible["nom_complet"])
        excel_presentation.cell(
            row=i + 2, column=2, value=cible["siege"]["date_creation"]
        )

        excel_membre.cell(row=i + 2, column=1, value=cible["nom_complet"])
        for num, membre in enumerate(cible["dirigeants"]):
            if cible["dirigeants"]:
                nom = membre.get("nom")
                prenoms = membre.get("prenoms")
                noms_prenoms = nom +" " + prenoms if nom and prenoms else nom if nom and not prenoms else prenoms 
            else:
                noms_prenoms = None
            excel_membre.cell(row= i+2, column = 2, value = noms_prenoms )

    excel.save("result.xlsx")
    return excel
