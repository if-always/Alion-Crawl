import re
import json
import requests
from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq
from Alion_Crawl.CRAW_FUNCTION.request import *

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}

def douban_movie(url):

    html = requests_text(url)
    soup = BeautifulSoup(html, "lxml")
    content = soup.find('div', class_='article')
    images = content.find_all('img')
    picture_name_list = [image['alt'] for image in images]
    #picture_link_list = [image['src'] for image in images]
    #urllib.request.urlretrieve(picture_link, '/home/lin/img/douban_books/%s.jpg' % picture_name)
    return picture_name_list

def news(url):

    html = requests_text(url)
    doc = pq(html)
    news = doc(".newsList ul li a").items()
    #print(news)
    news_list = [new.text() for new in news]
    #news_urls_list = [new.attr.href for new in news]
    #print(news_urls_list)
    return news_list

def jingdong_comment(url):

    comments = []
    html = requests_text(url)
    data = html.split('(', 1)[1]  # 去掉json不规范得地方
    data = data[0:len(data) - 2]
    data_json = json.loads(str(data))['comments']
    for i in list(range(len(data_json))):
        comment = data_json[i]['content']
        comments.append(comment)
    return comments

def maoyan_movie(url):

    movie_list = []
    html = requests_text(url)
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        movie_dict = {}
        movie_dict['index'] = item[0]
        movie_dict['image'] = item[1]
        movie_dict['title'] = item[2]
        movie_dict['actor'] = item[3].strip()[3:]
        movie_dict['times'] = item[4].strip()[5:]
        movie_dict['score'] = item[5] + item[6]
        movie_list.append(movie_dict)
    return movie_list

def picture(url):
    pic_list = []
    res = requests_json(url)
    if res.get('data'):
        for item in res.get('data'):
            title = item.get('title')
            pic_list.append(title)

    return pic_list

def novel_download(url):
    novel_list = []
    res = requests_text(url)
    #print(res)
    soup = BeautifulSoup(res, "lxml")
    info = soup.find('div', class_='wrapper_main')
    title = info.find('div',class_='h1title').h1.text.strip()[2:]

    print(items)
def sunan_job(url):
    job_list = []
    res = requests_text(url)
    infos = etree.HTML(res).xpath('//div[@class="dw_table"]/div[@class="el"]')
    for info in infos:
        try:
            items = {}
            items['posttime'] = info.xpath('.//span[@class="t5"]/text()')[0].strip()
            items['salary'] = info.xpath('.//span[@class="t4"]/text()')[0].strip()
            items['company'] = info.xpath('.//span[@class="t2"]/a[@target="_blank"]/text()')[0]
            items['workingplace'] = info.xpath('.//span[@class="t3"]/text()')[0][0:2].strip()
            items['jobname'] = info.xpath('.//p[@class="t1 "]/span/a[@target="_blank"]/text()')[0].strip()
            items['info_id'] = info.xpath('.//p[@class="t1 "]/span/a/@href')[0].strip()

            job_list.append(items)
        except :
            continue
    return job_list

# def douyin(url):
###
#     res_list = []
#     res = requests.get(url, headers=headers)
#     # print(res.content)
#     path = "./img/job_anal/" + url[-20:-8] + '.mp4'
#     with open(path, "wb") as file:
#         file.write(res.content)
#     info = str(url) + ".mp4 下载完成"
#     res_list.append(info)
#     return res_list
#qq