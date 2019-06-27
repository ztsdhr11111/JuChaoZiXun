
class Parse(object):
    def parse_1(self, response):
        base_url = 'http://static.cninfo.com.cn/'
        data = response.json()['classifiedAnnouncements']
        for i in data:
            for j in i:
                item = {}
                item['id'] = j['id']
                item['secCode'] = j['secCode']
                item['secName'] = j['secName']
                item['orgId'] = j['orgId']
                item['announcementId'] = j['announcementId']
                item['announcementTitle'] = j['announcementTitle']
                item['announcementTime'] = j['announcementTime']
                item['adjunctUrl'] = base_url + j['adjunctUrl']
                item['adjunctSize'] = j['adjunctSize']
                item['adjunctType'] = j['adjunctType']
                item['storageTime'] = j['storageTime']
                item['columnId'] = j['columnId']
                item['pageColumn'] = j['pageColumn']
                item['announcementType'] = j['announcementType']
                item['associateAnnouncement'] = j['associateAnnouncement']
                item['important'] = j['important']
                item['batchNum'] = j['batchNum']
                item['announcementContent'] = j['announcementContent']
                item['orgName'] = j['orgName']
                item['announcementTypeName'] = j['announcementTypeName']
                # print(item)
                yield item

    def parse_2(self, response):
        try:
            base_url = 'http://static.cninfo.com.cn/'
            data = response.json()['announcements']
            for j in data:
                item = {}
                item['id'] = j['id']
                item['secCode'] = j['secCode']
                item['secName'] = j['secName']
                item['orgId'] = j['orgId']
                item['announcementId'] = j['announcementId']
                item['announcementTitle'] = j['announcementTitle']
                item['announcementTime'] = j['announcementTime']
                item['adjunctUrl'] = base_url + j['adjunctUrl']
                item['adjunctSize'] = j['adjunctSize']
                item['adjunctType'] = j['adjunctType']
                item['storageTime'] = j['storageTime']
                item['columnId'] = j['columnId']
                item['pageColumn'] = j['pageColumn']
                item['announcementType'] = j['announcementType']
                item['associateAnnouncement'] = j['associateAnnouncement']
                item['important'] = j['important']
                item['batchNum'] = j['batchNum']
                item['announcementContent'] = j['announcementContent']
                item['orgName'] = j['orgName']
                item['announcementTypeName'] = j['announcementTypeName']
                # print(item)
                yield item
        except Exception as e:
            print('parse_2 error: {0}'.format(e))
            print(response.url)
            return None




    
    