import json
from requestApi.requestApi import requestApi


class generateToken():
    def __init__(self):
        readPass = open('pass.json')
        passData = json.load(readPass)
        headers = {'Content-Type': 'application/json'}
        obj = {'APIPassword': passData["pass"]}
        jsonData = json.dumps(obj).encode('utf8')
        url = f'token'
        self.response = requestApi().postRequest(jsonData, url, headers)

    def __call__(self):
        if (self.response.status_code == 200):
            return self.response.json()['Token']
        return f'Error:{self.response.status_code}'
