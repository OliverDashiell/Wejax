'''
Created on 11 Feb 2014

@author: dash
'''
import logging  # @UnresolvedImport
import tornado.ioloop
import tornado.web
from wejax.main_handler import MainHandler
from pkg_resources import resource_filename  # @UnresolvedImport
from wejax.websocket_handler import WebsocketHandler
from wejax.ajax_handler import AjaxHandler
from tornado.options import parse_command_line

def main():
    parse_command_line()
    
    settings = {
        "static_path": resource_filename('wejax',"www/static"),
        "template_path": resource_filename('wejax',"www"),
        "debug":True,
        "gzip":True
    }
    
    handlers = [
        (r"/", MainHandler),
        (r"/websocket", WebsocketHandler),
        (r"/ajax", AjaxHandler),
    ]
    
    application = tornado.web.Application(handlers, **settings)
    
    application.listen(8080)
    logging.info("Listening on 8080")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()