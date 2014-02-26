'''
Created on 11 Feb 2014

@author: dash
'''
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")