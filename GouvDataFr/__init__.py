import asyncio
import json
import os
import random
from itertools import chain
from urllib.parse import urlencode

import openpyxl
import pandas
from decouple import config
from loguru import logger
from requests.exceptions import ConnectionError, RequestException, Timeout

# from .utils_fr import MySheet
from utils import clear_terminal, env_HEADERS, return_entry, verify_entry, print_animate_texte

from .utils_fr import (
    ANNEE_DERNIERE,
    HEADER_FILL,
    HEADER_FONT,
    create_session,
    navigate_location,
)
from uuid import uuid4

ID_REQUETE = uuid4()

API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)
session = create_session()
