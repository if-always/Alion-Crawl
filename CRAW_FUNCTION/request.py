import chardet
import requests
from Alion_Crawl.UTIL import logutil
from Alion_Crawl.USER_PROXIE.user_agent import pass_useragent

def requests_text(url):

    headers = pass_useragent()
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            res.encoding = chardet.detect(res.content)['encoding']
            html = res.text
            return html
        else:
            logutil.error("网页错误" + str(res.status_code))
            return None
    except requests.ConnectionError:
        logutil.error("网页请求错误")

def requests_json(url):

    headers = pass_useragent()
    try:
        res = requests.get(url,headers=headers)

        if res.status_code == 200:
            return res.json()
        else:
            logutil.error("网页错误" + str(res.status_code))
            return None
    except requests.ConnectionError:
        logutil.error("网页请求错误")


