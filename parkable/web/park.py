# coding=UTF-8
'''
Created on 2013-9-7

@author: yezi
'''
import json
import string

from handler import BaseHandler

class ParkQueryHandler(BaseHandler):
    apiUrl = "http://api.dianping.com/v1/business/find_businesses"
    def get(self):
        langitude = self.get_argument("langitude", 0);
        latitude = self.get_argument("latitude", 0)
        keyword = self.get_argument("keyword", "")
        
        params = {"category" : "停车场", "city" : "北京"}
        if langitude > 0 and latitude > 0:
            params["langitude"] = langitude
            params["latitude"] = latitude
        if keyword :
            params["keyword"] = keyword
        
        url = self.requrl(self.apiUrl, params)
        
        dpdata = self.httpclient.fetch(url)

        retjson = json.loads(dpdata.body)
        
        self.finish(retjson)
        


class ParkCreateHandler(BaseHandler):
    pass


class ParkUpdateHandler(BaseHandler):
    def post(self):
        park_id = self.get_argument("park_id", "0");
        name = self.get_argument("name", "")
        address = self.get_argument("address", "")


class ParkInfoHandler(BaseHandler):
    apiUrl = "http://api.dianping.com/v1/business/get_single_business"
    def get(self, park_id):
        park_id = string.atoi(park_id)
        res = {}
        if park_id > 0:
            url = self.requrl(self.apiUrl, {"business_id" : str(park_id)})
            dpdata = self.httpclient.fetch(url)
            res = json.loads(dpdata.body)
        else :
            res["code"] = -1
            res["msg"] = "park_id cannot be null or 0"
                        
        self.finish(res);

