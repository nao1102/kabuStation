import requests
from requests.auth import HTTPBasicAuth
import configparser


class requestApi():
    def __init__(self,):
        inifile = configparser.SafeConfigParser()
        inifile.read('settings.ini')

        self.ipAddress = inifile.get('DEVELOP', 'ipaddress')
        basicUser = inifile.get('DEFAULT', 'basicUser')
        basicPass = inifile.get('DEFAULT', "basicPass")
        self.auth = HTTPBasicAuth(basicUser, basicPass)

    def getRequest(self, url, headers):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.get(url=fullUrl, headers=headers, auth=self.auth)

    def getRequestWithParams(self, url, headers, param):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.get(url=fullUrl, headers=headers, auth=self.auth, params=param)

    def postRequest(self, jsonData, url, headers):
        fullUrl = f'http://{self.ipAddress}/kabusapi/{url}'
        return requests.post(url=fullUrl, data=jsonData, headers=headers, auth=self.auth)
