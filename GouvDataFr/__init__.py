import json
import os
import openpyxl
from decouple import config
import asyncio
from utils import HEADERS, clear_terminal, navigate_location, return_entry, verify_entry
from urllib.parse import urlencode
import requests, json, pandas
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)