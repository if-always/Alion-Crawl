from urllib.parse import urlencode
import requests
def douban_movie_urls():
    start_urls = ["https://movie.douban.com/top250"]
    for i in range(1, 10):
        start_urls.append("https://movie.douban.com/top250?start=%d&filter=" % (25 * i))
    return start_urls

def news_urls():
    start_urls = ["http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml"]
    return start_urls


def jingdong_comment_urls():
    start_urls = []
    for i in range(1,20):
        start_urls.append('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv10452&productId=11794447957&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1'%i)
    return start_urls

def maoyan_movie_urls():
    start_urls = []
    for i in range(0,10):
        start_urls.append('http://maoyan.com/board/4?offset=' + str(i*10))
    return start_urls


def picture_url():
    start_urls = []
    for offset in range(1,21):
        params = {
            'offset':offset*20,
            'format':'json',
            'keyword':'街拍',
            'autoload':'true',
            'count':'20',
            'cur_tab':'1',

        }
        start_urls.append("http://www.toutiao.com/search_content/?" + urlencode(params))
    return start_urls

def novel_download_url():
    start_urls = []
    for id in range(3499508,3499510): #3501012
        start_urls.append("https://www.ybdu.com/xiaoshuo/13/13324/%d.html" %id)
    return start_urls


def sunan_job_url():
    start_urls = []
    for id in range(1,18):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%25A3%259F%25E5%2593%2581%25E6%25A3%2580%25E9%25AA%258C%25E5%2591%2598,2," + str(id) + ".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        start_urls.append(url)
    return start_urls


def douyin_url():
    start_urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
    }
    re = requests.get(
        "https://www.amemv.com/aweme/v1/aweme/post/?user_id=60973938437&count=21&max_cursor=0&aid=1128&_signature=pcwd0RAX.sTy-1WKa30BmaXMHc&dytk=397646b05e3aca84e4002ec64dd4533d",
        headers=headers).json()

    list = []
    # print(re['aweme_list'])
    for infos in re['aweme_list']:
        info = infos['video']['play_addr']
        url_id = info['uri']
        list.append(url_id)
    for url_id in list:
        url = "https://aweme.snssdk.com/aweme/v1/playwm/?video_id={}&line=0".format(url_id)
        start_urls.append(url)

    return start_urls
if __name__ == '__main__':
    urls = douyin_url()
    print (urls)
    pass