import requests

class Request(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    def request_get(self, url, headers=headers):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print('request_get error: {0}'.format(e))
    
    def request_post(self, url, headers=headers, data=None):
        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print('request_post error: {0}'.format(e))
 
