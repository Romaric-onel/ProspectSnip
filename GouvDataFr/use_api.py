from . import API_DATA_GOUV_FR,  asyncio, json, session, urlencode, Timeout, ConnectionError, RequestException
from .create_parameters import ask_scrap_information
from . import logger
SEMAPHORE = asyncio.Semaphore(5)
async def call_api(info, semaphore):
    query_string = urlencode(info)
    url = f"{API_DATA_GOUV_FR}search?{query_string}".replace("%2C", ",")

    async with semaphore:
        logger.debug("GET %s", url)
        try:
            response = await asyncio.to_thread(session.get, url, timeout=90)
            logger.debug("Response %s for %s ", response.status_code, url)
            response.raise_for_status()
            print(response.content)
            return response.json()

        except Timeout as e:
            logger.error("Timeout for %s: %s", url, e)
            print(e, url)
        except ConnectionError as e:
            logger.error("ConnectionError for %s: %s", url, e)
            print(e, url)
        except RequestException as e:
            body = getattr(response, "text", "<no body>")
            logger.error("RequestException for %s: %s — body: %s", url, e, body)
            print(e, url)
        return None


async def combine_all_result():
    info = ask_scrap_information()

    first_result = await call_api(info,SEMAPHORE)
    if not first_result:
        return []

    total_pages = first_result.get("total_pages", 1)
    tasks = [
        call_api({**info, "page": page},SEMAPHORE)
        for page in range (2, 8) #(2, total_pages + 1)
    ]
    rest_results = []
    if tasks:
        rest_results = await asyncio.gather(*tasks)
    session.close()
    results = [first_result] + [re_results for re_results in rest_results if re_results]

    return results