import requests
import lxml
from bs4 import BeautifulSoup, NavigableString
from download import *

#Various parameters for the url
def retrieve_results(title, FORMAT = "epub", LANGUAGE = "English", MIRROR_ID = "1"):
    results_dict = {}
    i = -1
    # Mimic a legitimate browser
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    # Search url: https://libgen.rs/fiction/?q=mistborn&criteria=&language=&format=epub
    url = "https://libgen.rs/fiction/?q=%"+ title + "&criteria=&language=" + LANGUAGE + "&format=" + FORMAT
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, "lxml")
    #TODO: Include ability to choose mirror_id

    tbody = soup.find('tbody')
    tr_items = tbody.children
    # Parse author information
    for tr in tr_items:
        # Ignore empty spaces in the code
        if isinstance(tr, NavigableString): continue
        i += 1
        results_dict[i] = []
        # Parse every column
        td_items = tr.find_all('td')
        for enum, td in enumerate(td_items):
            if enum == 5:
                mirror_link = td.find(text="[" + MIRROR_ID + "]").parent.get("href")
                results_dict[i].append(mirror_link)
                continue
            results_dict[i].append(td.text)

    return results_dict


    # download_req = requests.get(chosen_option_link, headers)
    # soup = BeautifulSoup(download_req.content, "lxml")
    # download_link = soup.find(text="GET").parent.get('href')

    # download.getFile(download_link)

