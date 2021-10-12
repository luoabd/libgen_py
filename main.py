import argparse
import requests
import lxml
from bs4 import BeautifulSoup
from download import *

parser = argparse.ArgumentParser(description='Search and Download books from libgen.')
parser.add_argument('title', type=str, nargs='?', default='tree',
                    help='The title of the book you are searching for')

args = parser.parse_args()

# Mimic a legitimate browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Search url: http://libgen.rs/?search.php&req=name
url = "http://libgen.rs/?search.php&req=%s"%args.title
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, "lxml")
mirror_link = soup.find(text="[1]").parent.get('href')

download_req = requests.get(mirror_link, headers)
soup = BeautifulSoup(download_req.content, "lxml")
download_link = soup.find(text="GET").parent.get('href')

download.getFile(download_link)

