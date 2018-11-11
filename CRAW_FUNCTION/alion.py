'''
author ：alion
函数主程序 ， 主要通过para_dict中的值调用其它函数完成操作
'''


import os
from time import time
from Alion_Crawl.UTIL import logutil
from Alion_Crawl.THREAD_CURRENT import current


def qaaq(dict_name,th_num):
    start_time = time()
    logutil.info("正在获取目标url列表")
    try:
        starts_url = dict_name.get('url_list')()
        #print(starts_url)
        if len(starts_url) >= 1:
            logutil.info("目标url列表获取成功")
        else:
            logutil.warning("目标url列表为空")
            os._exit(1)
    except:
        logutil.error("目标url列表获取错误")
        os._exit(1)
    try:
        func_name = dict_name.get('func_name')
        logutil.info("目标处理函数获取成功")
        logutil.info("正在分配线程 , 线程数：%d" %th_num)
        res = current.currents(func_name,starts_url,th_num)
        #if save_type is str:
        dict_name.get('save_type')(res,dict_name.get('save_path'),dict_name.get('id_name'))
        logutil.info(res)
    except:
        logutil.error("目标处理函数获取失败")
        os._exit(1)
    end_time = time()
    logutil.info('Cost {} seconds'.format((end_time - start_time)))