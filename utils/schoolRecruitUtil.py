import requests
import urllib3
from pyquery import PyQuery

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
BULLETIN_URL = 'https://bulletin.site.nthu.edu.tw/p/403-1086-5075-1.php?Lang=zh-tw'

def get_list():
    data = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    html = requests.get(BULLETIN_URL, headers=headers, verify=False)

    dom = PyQuery(html.content)
    recruitments = dom('#pageptlist .listBS').items()

    for item in recruitments:
        date = item('.mdate.before').text()

        url_dom = item('a')
        title = url_dom.text()
        url = url_dom.attr.href

        data.append({
            'date': date,
            'title': title,
            'url': url
        })

    return data