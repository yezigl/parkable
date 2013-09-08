#coding=UTF-8
'''
Created on 2013-9-2

@author: yezi
'''
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

from tornado.options import define, options

import web.handler
import web.park
import web.comment

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="parkable database host")
define("mysql_database", default="parkable", help="parkable database name")
define("mysql_user", default="parkable", help="parkable database user")
define("mysql_password", default="parkable", help="parkable database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", web.handler.HomeHandler),
            (r"/v1/park/query", web.park.ParkQueryHandler),
            (r"/v1/park/create", web.park.ParkCreateHandler),
            (r"/v1/park/update", web.park.ParkUpdateHandler),
            (r"/v1/park/([\d]+)", web.park.ParkInfoHandler),
            (r"/v1/comment/create", web.comment.CommentCreateHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__PARKABLE!*#&$**WE&__",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
#        self.db = torndb.Connection(
#            host=options.mysql_host, database=options.mysql_database,
#            user=options.mysql_user, password=options.mysql_password)
        
        self.httpclient = tornado.httpclient.HTTPClient()


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
if __name__ == '__main__':
    main()
