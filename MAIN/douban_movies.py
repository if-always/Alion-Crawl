
from Alion_Crawl.CRAW_FUNCTION.alion import qaaq
from Alion_Crawl.UTIL.param_dict import *


'''
@三个参数 ：设置的函数名 、url函数名 、启动的线程数目
'''
if __name__ == '__main__':

    dict_name = douban_movie
    qaaq(dict_name,10)
#qaaq