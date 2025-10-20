import json

from decouple import config

from utils import HEADERS, clear_terminal, navigate_location, return_entry, verify_entry
from urllib.parse import urlencode, urljoin

API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)