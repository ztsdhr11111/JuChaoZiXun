import csv
from mongo_client import all_simi
from mongo_utils import save

file = ''

with open(file, 'r', encoding='utf-8') as f:
    data = csv.DictReader(f)
    for i in data:
        # print(i)
        # print(type(i))
        save(all_simi, i)
        break
    
# print(type(data))
