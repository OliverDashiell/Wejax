'''
Created on 11 Feb 2014

@author: dash
'''
from tornado import websocket
import time
import logging  # @UnresolvedImport


class WebsocketHandler(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        timestamp = time.time()
        self.write_message(u"You said: " + message)
        logging.info("/websocket %0.5fms", time.time()-timestamp)

    def on_close(self):
        print "WebSocket closed"