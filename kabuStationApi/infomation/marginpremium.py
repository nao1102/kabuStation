from requestApi import requestApi


class marginpremium():
    def __init__(self, code, token):
        urlSymbol = f'margin/marginpremium/{code}'
        self.req = requestApi().getRequest(urlSymbol, {'X-API-KEY': token})

    def __call__(self, str):
        if(self.req.status_code==200):
            if str == "":
                return self.req.json()
            else:
                return self.req.json()[str]
        return f'Error:{self.req.status_code}'
