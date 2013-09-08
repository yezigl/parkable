#coding=UTF-8
'''
Created on 2013-9-7

@author: yezi
'''

import tornado.web
import hashlib
import urllib

class BaseHandler(tornado.web.RequestHandler):
    APP_KEY = "398438032"
    APP_SECRET = "c5a1fe250e5849d998ff75a06f043e1b"
#    @property
#    def db(self):
#        return self.application.db
    
    @property
    def httpclient(self):
        return self.application.httpclient
    
    def requrl(self, apiUrl, params):
        codec = self.APP_KEY
        for key in sorted(params.iterkeys()):
            codec += key + params[key]
        codec += self.APP_SECRET
        
        sign = (hashlib.sha1(codec).hexdigest()).upper()
        
        urlTrail = "appkey=" + self.APP_KEY + "&sign=" + sign
#        for (key, value) in kwargs.items():
        urlTrail += "&" + urllib.urlencode(params)
        
        requrl = apiUrl + "?" + urlTrail
        print requrl
        return requrl
    


class HomeHandler(BaseHandler):
    def get(self):
        self.finish("Hello World!!!")