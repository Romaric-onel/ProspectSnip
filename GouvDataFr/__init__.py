import asyncio
import json
import os
import random
from itertools import chain
from urllib.parse import urlencode

import openpyxl
import pandas
from decouple import config
from requests.exceptions import ConnectionError, RequestException, Timeout
from loguru import logger
from utils import (
    HEADERS,
    clear_terminal,
    create_session,
    navigate_location,
    return_entry,
    verify_entry,
)

ID_REQUETE = random.randint(100000000, 100000000)
API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)
session = create_session()
