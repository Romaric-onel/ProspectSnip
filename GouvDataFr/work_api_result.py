from openpyxl.workbook.workbook import Workbook

from . import asyncio, chain, json, openpyxl, os, pandas, ANNEE_DERNIERE
from .use_api import combine_all_result

start = 0


def resultat_to_sheet():
    global start
    raw_data = asyncio.run(combine_all_result())
    data = list(chain.from_iterable(item["results"] for item in raw_data))

    # création du fichier excel
    excel = openpyxl.Workbook()

    # création des feuilles sheet

    excel_presentation: Workbook = excel.active  # type: ignore
    excel_membre: Workbook = excel.create_sheet(title="Membre")  # type: ignore
    excel_finance: Workbook = excel.create_sheet(title=f"Finance {ANNEE_DERNIERE}")

    # ....
    excel_presentation.title = "Présentation"  # type: ignore

    # remplir les feuilles
    for i, cible in enumerate(data):
        # données
        name = cible["nom_complet"]
        members = [member for member in cible["dirigeants"]]
       
        try:
            finance = cible["finances"]["ANNEE_DERNIERE"] 
        except:
            finance = {'ca': None, 'resultat_net': None}
        # data[93]['']
        # remplissage feuille 1
        excel_presentation.cell(row=i + 2, column=1, value=name)
        excel_presentation.cell(
            row=i + 2, column=2, value=cible["siege"]["date_creation"]
        )
        excel_presentation.cell(row=i + 2, column=3, value=cible["siege"]["adresse"])
        excel_presentation.cell(
            row=i + 2, column=2, value=cible["siege"]["date_debut_activite"]
        )
        # remplissage

        if members:

            excel_membre.cell(row=2 + start, column=1, value=name)
            excel_membre.merge_cells(
                start_row=2 + start,
                end_row=2 + start + len(members) - 1,
                start_column=1,
                end_column=1,
            )

            num = start

            for membre in members:
                # données
                nom = membre.get("nom")
                prenoms = membre.get("prenoms")
                qualite = membre.get("qualite")
                type = membre.get("type_dirigeant")
                naissance = membre.get("annee_de_naissance")
                denomination = membre.get("denomination")
                # data[2]['dirigeants'][4]['denomination']
                # remplissage
                excel_membre.cell(row=num + 2, column=2, value=nom)
                excel_membre.cell(row=num + 2, column=3, value=prenoms)
                excel_membre.cell(row=num + 2, column=4, value=qualite)
                excel_membre.cell(
                    row=num + 2,
                    column=5,
                    value=(
                        "✅"
                        if type == "personne physique"
                        else "❌" if type == "personne morale" else None
                    ),
                )

                excel_membre.cell(
                    row=num + 2,
                    column=6,
                    value=int(naissance) if naissance else naissance,
                )
                if nom is None and prenoms is None:
                    excel_membre.cell(row=num + 2, column=2, value=denomination)
                    """excel_membre.merge_cells(
                        start_row=num,
                        end_row=num,
                        start_column=2,
                        end_column=3,
                    )"""
                num += 1
        else:
            excel_membre.cell(row=start + 2, column=2, value=None)
        start += len(members) + 1

        # remplissage feuille 3
        excel_finance.cell(row=i + 2, column=1, value=name)
        excel_finance.cell(row=i + 2, column=2, value=finance["ca"])
        excel_finance.cell(row=i + 2, column=3, value=finance["resultat_net"])
        

    excel.save("result.xlsx")
    return excel


