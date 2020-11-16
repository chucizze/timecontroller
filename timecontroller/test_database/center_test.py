import unittest
import json
import http.client as httplib
import urllib.parse as urllib
from conf import httpserver
from conf import httpport
import urllib

conn = httplib.HTTPConnection(httpserver, httpport)
header = {"Content-type": "application/x-www-form-urlencoded"}

class TestCenter(unittest.TestCase):


   # def test_personalcencer(self):
   #     global conn
   #     conn.request('GET', '/v1/timecontroller/personalcenter/show/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa')
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])


   # def test_ownattention(self):
   #     global conn
   #     conn.request('GET', '/v1/timecontroller/ownattention/show/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa')
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
#        
        
#        
#    def test_cancleattention(self):
#        global conn
#        global header
#        params = {"usertoken_str": "c341eda1-cd8d-48ae-bbc4-c668de8f59fa","user_id":"2"}
#        params = urllib.parse.urlencode(params)
#        conn.request('POST', '/v1/timecontroller/cancel/attentionbutton/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
        
        
        
#        
#    def test_addattention(self):
#        global conn
#        global header
#        params = {"usertoken_str":"c341eda1-cd8d-48ae-bbc4-c668de8f59fa","user_id":"2"}
#        params = urllib.parse.urlencode(params)
#        conn.request('POST', '/v1/timecontroller/add/attentionbutton/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])

#        
#        
#    def test_ownfans(self):
#        global conn
#        conn.request('GET', '/v1/timecontroller/ownfans/show/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa')
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])



   def test_showotherinfo(self):
       global conn
       conn.request('GET', '/v1/timecontroller/otherinfo/showinfo/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa&userid=1')
       data = json.loads(conn.getresponse().read().decode("utf-8"))
       print(data)
       self.assertTrue(data["infostatus"])
