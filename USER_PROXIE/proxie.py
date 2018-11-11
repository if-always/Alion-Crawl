import requests
import json
# 请求API，并解析json成dictionary
proxy_result = requests.get("http://proxy.nghuyong.top").json()
print(proxy_result)
num = proxy_result['num']
updatetime = proxy_result['updatetime']
proxy_data = proxy_result['data']
# 获取其中一个代理
one_proxy = proxy_data[0]
print(one_proxy)
# 爬虫加上代理
requests.get("http://www.baidu.com",proxies={"http":one_proxy['type']+"://"+one_proxy['ip_and_port']})
