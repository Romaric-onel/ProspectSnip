import asyncio
import json
import os
import random
from itertools import chain
from urllib.parse import urlencode
from .utils_fr import ANNEE_DERNIERE
import openpyxl
import pandas
from decouple import config
from loguru import logger
from requests.exceptions import ConnectionError, RequestException, Timeout
#from .utils_fr import MySheet
from utils import HEADERS, clear_terminal, return_entry, verify_entry
from .utils_fr import EMPTY_ROW_STYLE, create_session, navigate_location

ID_REQUETE = random.randint(100000000, 100000000)
API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)
session = create_session()
