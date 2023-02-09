from requestApi.requestApi import requestApi


class board():
    def __init__(self, market, code, token):
        urlSymbol = f'board/{code}@{market}'
        self.req = requestApi().getRequest(urlSymbol, {'X-API-KEY': token})

    def __call__(self, str):
        if(self.req.status_code==200):
            if str == "":
                return self.req.json()
            else:
                return self.req.json()[str]
        return f'Error:{self.req.status_code}'
