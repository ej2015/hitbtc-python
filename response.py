from requests import Response

class CustomResponse():
    def __init__(self, res):
        self.res = res

    def response(self):
        if self.res.ok:
            return self.res.json()
        else:
            return f"{self.res.status_code}: {self.res.content}"
