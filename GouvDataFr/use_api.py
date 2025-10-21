from .create_parameters import  ask_scrap_information
from . import urlencode, urljoin, API_DATA_GOUV_FR

def main():
    info = ask_scrap_information()

    query_string = urlencode(info)

    url = f"{API_DATA_GOUV_FR}search?{query_string}".replace("%2C", ",")
    print(url)