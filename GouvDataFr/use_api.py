from .create_parameters import  ask_scrap_information
from . import urlencode, urljoin, API_DATA_GOUV_FR, json, pandas, requests
from . import os, openpyxl
def call_api_and_decode_result(info):
    query_string = urlencode(info)
    url = f"{API_DATA_GOUV_FR}search?{query_string}".replace("%2C", ",")

    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return json.loads(response.content.decode("utf-8"))
    
    except requests.exceptions.Timeout:
        print("Votre machine présente un souci pour retourner la ressource\n.Réessayez puis contactez Hounsinou Romaric Onel si le problème persiste")
    except requests.exceptions.ConnectionError:
        print("Vous n'êtes pas connecté à Internet")
    
    except requests.exceptions.RequestException:
        print("Un souci particulier se pose.\nEffectuez une capture d'écran, puis envoyez à Hounsinou Romaric Onel sur LinkedIn pour une assistance")
    
    
    return None

def combine_all_result():
    info = ask_scrap_information()
    all_resultats = []
    while True:
        print(info)
        results = call_api_and_decode_result(info)
        info["page"] += 1
        if info["page"] > results ["total_pages"]:
            break
        
        
        if results:
            all_resultats.append(results)
        print(all_resultats)
    return all_resultats
    
    # with open("resultat_vf.json", "w", encoding="utf-8") as f:
    #     json.dump(json.loads(results), f, indent=4, ensure_ascii=False)