from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from Alion_Crawl.UTIL import logutil


res_list = []


def currents(func,args,nums):

    executor = ThreadPoolExecutor(max_workers=nums)

    future_tasks = [executor.submit(func, arg) for arg in args]

    wait(future_tasks, return_when=ALL_COMPLETED)

    for res in future_tasks:
        #print("@")
        logutil.info(res.done())
        logutil.info(res.result())
        res_list.extend(res.result())
    return res_list