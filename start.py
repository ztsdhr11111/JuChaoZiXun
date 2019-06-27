import time
import random
from math import ceil
from multiprocessing.pool import Pool

from base_request import Request
from base_parse import Parse
from mongo_client import collection
from mongo_utils import save


def _structure_urls():
    # base_url = 'http://www.cninfo.com.cn/new/disclosure?column=szse_latest&pageNum={0}&pageSize=20'
    base_url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query?pageNum={0}&pageSize=30&tabName=fulltext&column=szse&plate=sz&seDate=2016-01-01+~+2019-03-23'
    page = ceil(915970/30)
    for i in range(1, page):
        url = base_url.format(i)
        yield url

def _request(url):
    request = Request()
    response = request.request_post(url)
    return response

def _parse(response):
    parse = Parse()
    items = parse.parse_2(response)
    return items

def run(url):
    response = _request(url)
    items = _parse(response)
    for item in items:
        print(item)
        # save(collection, item)
    time.sleep(random.choice(range(10)))

if __name__ == "__main__":
    urls = _structure_urls()
    pool = Pool()
    pool.map(run, urls)
    pool.close()
    pool.join()
#     for url in urls:
#         response = _request(url)
#         items = _parse(response)
#         if items is not None:
#             for item in items:
#                 save(collection, item)
#         time.sleep(random.choice(range(10)))

