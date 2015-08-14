#!/usr/bin/env python2.7

import sys
import json
import ConfigParser
import tornado.ioloop
from tornado_json.routes import get_routes
from tornado_json.application import Application

cfg = ""
try:
    cfg = sys.argv[1]
except:
    cfg = "app.cfg"

print "cfg: " + cfg

Config = ConfigParser.ConfigParser()
Config.read(cfg)

port = Config.get("config", "port")
token = ""

try:
    token = sys.argv[2]
except:
    token = Config.get("config", "token")

def main():
    import helloworld

    routes = get_routes(helloworld)
    #    routes.extend(get_routes(git))
        
    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )
    application = Application(routes=routes, settings={'token': token})

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
