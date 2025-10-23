from . import asyncio, openpyxl, os, pandas, json
from .use_api import combine_all_result
from . import chain
from openpyxl.workbook.workbook import Workbook 
def resultat_to_sheet():
    raw_data = asyncio.run(combine_all_result())
    data = list(chain.from_iterable(item["results"] for item in raw_data))
    
    
    excel = openpyxl.Workbook()
    

    # with open ("resultats.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    excel_presentation : Workbook= excel.active #type: ignore
    excel_membre : Workbook= excel.create_sheet() #type: ignore

    excel_presentation.title = "Présentation" #type: ignore
    for i, cible in enumerate(data):
        excel_presentation.cell(row = i+2, column=1, value=cible ["nom_complet"])
        excel_presentation.cell(row = i+2, column=2, value=cible ["siege"]["date_creation"])


    for i, cible in enumerate(data):
        excel_membre.cell(row = i+2, column = 1, value = cible["nom_complet"])


    excel.save("result.xlsx")
    return excel