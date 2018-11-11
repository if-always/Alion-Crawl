from Alion_Crawl.CRAW_FUNCTION import all_functions
from Alion_Crawl.UTIL import starts_urls
from Alion_Crawl.DATAS_HANDLES import datas_save

'''
模块字典 ， 每个字典对应每个main主函数，需要在函数执行前完成初始化 ， 有5个键值对：all_functions中的主爬取函数 、
获取url列表函数 、结果存储方式 、 存储路径 、以及id_name（这个是csv存储特有的）
'''


fenghuang_news = {
    "func_name":all_functions.news,
    "url_list":starts_urls.news_urls,
    "save_type":datas_save.text_save,
    "save_path":"./img/news.text",
    "id_name":''
}

jingdong_comments = {
    "func_name":all_functions.jingdong_comment,
    "url_list":starts_urls.jingdong_comment_urls,
    "save_type":datas_save.text_save,
    "save_path":"./img/comments.text",
    "id_name":''
}


douban_movie = {
    'func_name':all_functions.douban_movie,
    'url_list':starts_urls.douban_movie_urls,
    'save_type':datas_save.text_save,
    'save_path':'./img/qaaq.text',
    'id_name':''
}


maoyan_movie = {
    'func_name':all_functions.maoyan_movie,
    'url_list':starts_urls.maoyan_movie_urls,
    'save_type':datas_save.csv_save,
    'save_path':'./img/qaaq123.csv',
    'id_name':['index', 'image', 'title','actor','times','score']
}

picture = {
    'func_name':all_functions.picture,
    'url_list':starts_urls.picture_url,
    'save_type':datas_save.json_save,
    'save_path':'./img/pic.json',
    'id_name':''
}

novel_download = {
    'func_name':all_functions.novel_download,
    'url_list':starts_urls.novel_download_url,
    'save_type':datas_save.text_save,
    'save_path':'./img/novel.text',
    'id_name':''
}

sunan_job = {
    'func_name':all_functions.sunan_job,
    'url_list':starts_urls.sunan_job_url,
    'save_type':datas_save.json_save,
    'save_path':'./img/sunan/check.json',
    'id_name':['info_id','salary','jobname','workingplace','company','posttime']
}

douyin = {
    'func_name':all_functions.douyin,
    'url_list':starts_urls.douyin_url,
    'save_type':datas_save.text_save,
    'save_path':'',
    'id_name':''
}