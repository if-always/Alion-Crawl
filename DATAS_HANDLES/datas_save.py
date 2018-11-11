import csv
import json

'''
@res 为返回值列表
@path 为文件存储路径
'''

def pic_save(res,path,idname):
    for id in res:
        path = path + str(id[-4:]) + '.mp4'
        with open(path,'a',encoding='utf-8') as file:
            file.write(id.content)

def text_save(res,path,id_name):
    pass
    #datas = ''
    #for data in res:
    #    datas = datas + data + '\n'
    #with open(path,'a',encoding='utf-8') as file:
    #    file.write(datas)



def json_save(res,path,id_name):
    with open(path,'w',encoding='utf-8') as file:
        for js in res:
            file.write(json.dumps(js,indent=2,ensure_ascii=False))
            #indent = 2  代表缩进字符个数
            #ensure_ascii = False 为了显示中文


def csv_save(res,path,id_name):
    with open(path, 'w',encoding='utf-8') as csvfile:
        fieldnames = id_name#['index', 'image', 'title','actor','times','score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in res:
            writer.writerow(i)


def mysql_save():
    pass