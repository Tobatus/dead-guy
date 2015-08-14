from tornado_json.requesthandlers import APIHandler

class TowerAPIHandler(APIHandler):
    __url_names__ = ["helloworld"]

class Handler(TowerAPIHandler):
    def get(self):
        try:
            self.success("hello world")
        except:
            self.fail("Failed")

class UpdateHandler(TowerAPIHandler):
    def get(self, token, key, value):
        try:
            if (token == self.application.settings['token']):
                print key + ": " + value + "\n"
                self.success("Success")
            else:
                raise Error("Not supported")
        except:
            self.fail("Failed")

class GetHandler(TowerAPIHandler):
    def get(self, token, key):
        try:
            if (token == self.application.settings['token']):
                print key + "\n"
                self.success("Success")
            else:
                raise Error("Not supported")
        except:
            self.fail("Failed")
