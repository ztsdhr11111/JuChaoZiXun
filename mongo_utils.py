


def view_all(collection):
    '''
    查询所有数据
    '''
    num = collection.find()
    return num

def view_status(collection, status):
    '''
    查询指定状态的信息
    '''
    item = collection.find({'status': status})
    return item

def update(collection, query, update):
    '''
    修改字段值
    '''
    try:
        collection.update(query, {'$set': update})
        print('修改成功')
    except Exception as e:
        print('update error: {0}'.format(e))

def deleteOne(collection, query):
    '''
    删除一组数据
    '''
    try:
        collection.remove(query)
        print('删除成功')
    except Exception as e:
        print(e)


def save(collection, item):
    '''
    保存数据
    '''
    try:
        collection.insert_one(item)
        print('Successful')
    except Exception as e:
        print(e)
        print('Faild')
