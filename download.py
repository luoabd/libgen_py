import requests
import re

class download():
    # Mimic a legitimate browser
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    def getFilename_fromCd(cd):
        """
        Get filename from content-disposition
        """
        if not cd:
            return None
        fname = re.findall('filename=(.+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]

    def getFile(download_link):
        r = requests.get(download_link, download.headers)
        filename = download.getFilename_fromCd(r.headers.get('content-disposition'))
        open(filename[1:-1], 'wb').write(r.content)
