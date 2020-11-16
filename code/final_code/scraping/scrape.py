from urllib.error import HTTPError
from urllib.request import Request, urlopen
import requests
import os

HEADERS = {'User-Agent': 'Safari/537.3'}

def write_to_file(data, fp):
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    f = open(fp, 'wb')
    if (data):
        f.write(data)
        f.close()

def get_html(url, headers):
    req = Request(url=url, headers=headers)
    # read the data from the URL and write to a file
    try:
        webpage = urlopen(req)
        data = webpage.read()
    except HTTPError as err:
        if (err.code == 404):
            print(err)
            data = None
        else:
            data = None
    return data

def write_html_to_file(url, headers, fp):
    data = get_html(url, headers)
    write_to_file(data, fp)