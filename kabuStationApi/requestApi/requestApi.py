import requests
from requests.auth import HTTPBasicAuth
import json
import configparser

class requestApi():
    def __init__(self,):
        inifile = configparser.SafeConfigParser()
        inifile.read('../../settings.ini')
        ipAddress=inifile.get('DEVELOP', 'ipaddress')
        print(ipAddress)
        readPass = open('pass.json')
        passData = json.load(readPass)
        self.ipAddress = passData["ipaddress"]
        self.auth = HTTPBasicAuth(passData["basicUser"], passData["basicPass"])

    def getRequest(self, url, headers):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.get(url=fullUrl, headers=headers, auth=self.auth)
    
    def getRequestWithParams(self, url, headers,param):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.get(url=fullUrl, headers=headers, auth=self.auth,params=param)

    def postRequest(self, jsonData, url, headers):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.post(url=fullUrl, data=jsonData, headers=headers, auth=self.auth)
