from tornado_json.requesthandlers import APIHandler

class TowerAPIHandler(APIHandler):
    __url_names__ = ["tower"]

class Handler(TowerAPIHandler):
    def get(self):
        try:
            self.success("hello world")
        except:
            self.fail("Failed")
