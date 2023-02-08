import json
from requestApi.requestApi import requestApi


class generateToken():
    def __init__(self):
        readPass = open('pass.json')
        passData = json.load(readPass)
        headers = {'Content-Type': 'application/json'}
        obj = {'APIPassword': passData["pass"]}
        jsonData = json.dumps(obj).encode('utf8')
        url = f'/kabusapi/token'
        response = requestApi().postRequest(jsonData, url, headers)
        self.token = response.json()['Token']

    def __call__(self):
        return self.token
