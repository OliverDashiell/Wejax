'''
Created on 11 Feb 2014

@author: dash
'''
import tornado.web


class AjaxHandler(tornado.web.RequestHandler):
    def get(self):
        message = self.get_argument("msg", "Hello, ajax")
        self.write(u"You said: " + message)