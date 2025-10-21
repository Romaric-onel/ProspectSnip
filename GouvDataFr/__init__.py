import json
import os
import openpyxl
from decouple import config
import asyncio
from utils import HEADERS, clear_terminal, navigate_location, return_entry, verify_entry
from urllib.parse import urlencode, urljoin
import requests, json, pandas
API_DATA_GOUV_FR = config("ApiGouvEntreprise", cast=str, default=None)