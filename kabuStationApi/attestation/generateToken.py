import json
from ..requestApi import requestApi
import configparser


class generateToken():
    def __init__(self):
        inifile = configparser.SafeConfigParser()
        inifile.read('settings.ini')
        passWord = inifile.get('DEFAULT', "pass")
        headers = {'Content-Type': 'application/json'}
        obj = {'APIPassword': passWord}
        jsonData = json.dumps(obj).encode('utf8')
        url = f'token'
        requestApiItem = requestApi()
        self.response = requestApiItem.postRequest(jsonData, url, headers)

    def __call__(self):
        if (self.response.status_code == 200):
            return self.response.json()['Token']
        return f'Error:{self.response.status_code}'
