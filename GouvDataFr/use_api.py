from . import API_DATA_GOUV_FR,  asyncio, json, session, urlencode, Timeout, ConnectionError, RequestException
from .create_parameters import ask_scrap_information
from . import logger
from .utils_fr import rotate_header, random
SEMAPHORE = asyncio.Semaphore(4)
async def call_api(info, semaphore):
    query_string = urlencode(info)
    url = f"{API_DATA_GOUV_FR}search?{query_string}".replace("%2C", ",")
    sessionH = rotate_header(session)
    await asyncio.sleep(random.uniform(1, 2))
    async with semaphore:
        logger.debug(f"La requête vers l'URL {url} a commencée")
        try:
            response = await asyncio.to_thread(sessionH.get, url, timeout=300)
            logger.debug(f"Response {response.status_code} for {url}")
            response.raise_for_status()
            print(response.json())
            #print(url)
            return response.json()

        except Timeout as e:
            logger.exception(f"Timeout for {url}: {e}")
            print(e, url)
        except ConnectionError as e:
            logger.exception(f"ConnectionError for {url}: {e}")
            print(e, url)
        except RequestException as e:
            logger.exception(f"RequestException for {url}: {e}")
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
        for page in range (2, total_pages) #(2, 3) #
    ]
    rest_results = []
    if tasks:
        rest_results = await asyncio.gather(*tasks)
    session.close()
    results = [first_result] + [re_results for re_results in rest_results if re_results]

    return results