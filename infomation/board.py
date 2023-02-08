from requestApi.requestApi import requestApi

class board():
    def __init__(self, market, code, token):
        urlSymbol = f'/kabusapi/symbol/{code}@{market}'
        self.req = requestApi().getRequest(urlSymbol, {'X-API-KEY': token})

    def __call__(self,str):
        if str=="":
            return self.req.json()
        else:
            return self.req.json()[str]