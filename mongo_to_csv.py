import os
import csv

from mongo_client import collection
from mongo_utils import view_all

def get_headers(collection):
    '''
    获取字典头
    '''
    headers = []
    data = view_all(collection)
    for i in data:
        for j in i.keys():
            headers.append(j)
        break
    return headers

def get_content(collection):
    '''
    获取内容
    '''
    contents = []
    data = view_all(collection)
    for i in data:
        content = []
        for j in i.values():
            content.append(j)
        contents.append(content)
    return contents

def save_to_csv(file, item):
    '''
    保存到csv文件
    '''
    if not os.path.exists:
        with open(file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(item)
    else:
        with open(file, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            i = 1
            for content in item:
                print(content)
                writer.writerow(content)
                print('Successful：{0}'.format(i))
                i += 1
        print('保存完毕')


if __name__ == "__main__":
    file = 'cninf.csv'
    headers = get_headers(collection)
    print(headers)
    save_to_csv(file, [headers])
    contents = get_content(collection)
    save_to_csv(file, contents)