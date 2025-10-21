from .create_parameters import  ask_scrap_information
from . import urlencode, urljoin, API_DATA_GOUV_FR, json, pandas, requests
from . import os, openpyxl, asyncio
async def call_api_and_decode_result(info):
    query_string = urlencode(info)
    url = f"{API_DATA_GOUV_FR}search?{query_string}".replace("%2C", ",")

    
    try:
        response = await asyncio.to_thread(requests.get, url, timeout=15)
        response.raise_for_status()
        print(response.content)
        return json.loads(response.content.decode("utf-8"))
    
    except requests.exceptions.Timeout:
        print("Votre machine présente un souci pour retourner la ressource\n.Réessayez puis contactez Hounsinou Romaric Onel si le problème persiste")
    except requests.exceptions.ConnectionError:
        print("Vous n'êtes pas connecté à Internet")
    
    except requests.exceptions.RequestException:
        print("Un souci particulier se pose.\nEffectuez une capture d'écran, puis envoyez à Hounsinou Romaric Onel sur LinkedIn pour une assistance")
    
    
    return None

async def combine_all_result():
    info = ask_scrap_information()
    
    first_result = await call_api_and_decode_result(info)
    if not first_result:
        return []

    total_pages = first_result.get("total_pages", 1)
    tasks = [
        call_api_and_decode_result({**info, "page": page})
        for page in range(2, total_pages + 1)
    ]
    rest_results = []
    if tasks:
        rest_results = await asyncio.gather(*tasks, return_exceptions=True)

    return [first_result] + rest_results