import unittest
import json
import http.client as httplib
import urllib.parse as urllib
from conf import httpserver
from conf import httpport
import urllib

conn = httplib.HTTPConnection(httpserver, httpport)
header = {"Content-type": "application/x-www-form-urlencoded"}

class TestForum(unittest.TestCase):
   #
   def test_forumdefshow(self):
       global conn
       conn.request('GET', '/v1/forum/defshow/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa')
       data = json.loads(conn.getresponse().read().decode("utf-8"))
       print(data)
       self.assertTrue(data["infostatus"])
        
        

   # def test_forumdefshow(self):
   #     global conn
   #     conn.request('GET', '/v1/forum/showme/?usertoken_str=555558ea-d7f7-41dd-80e3-ad14e799bb8e')
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
#        
        
   # def test_forumcommentpublis(self):
   #     global conn
   #     global header
   #     params = {"forum_id":"1","usertoken_str":"c341eda1-cd8d-48ae-bbc4-c668de8f59fa","comment_context":"帖子测试"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST', '/v1/forum/comment/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])



   # def test_PublishForum(self):
   #     global conn
   #     global header
   #     params = {"usertoken_str":"c341eda1-cd8d-48ae-bbc4-c668de8f59fa","forum_title":"这是新加的论坛帖子主题","forum_desp":"这是论坛内容，差距从不会vbowppiqhchaohcfo1查看虐一飞机无法"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST', '/v1/forum/publish/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
   #
        
        
   # def test_forumallshow(self):
   #     global conn
   #     conn.request('GET', '/v1/forum/detailshow/?usertoken_str=c341eda1-cd8d-48ae-bbc4-c668de8f59fa&forum_id=1')
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
#        
#        
#    def test_forumpraise(self):
#        global conn
#        global header
#        params = {"usertoken_str":"5d6d58ea-d7f7-41dd-80e3-ad14e799bb8e",
#                  "forum_id":1,
#                  "praise_status":0}
#        params = urllib.parse.urlencode(params)
#        conn.request('POST', '/v1/forum/praise/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])


#        
#    def test_delectforum(self):
#        global conn
#        global header
#        params = {"usertoken_str": "c341eda1-cd8d-48ae-bbc4-c668de8f59","forum_id":"5"}
#        params = urllib.parse.urlencode(params)
#        conn.request('POST', '/v1/forum/deleteforum/', params, header)
#        data = json.loads(conn.getresponse().read().decode("utf-8"))
#        print(data)
#        self.assertTrue(data["infostatus"])
        
   # def test_modifyforum(self):
   #     global conn
   #     global header
   #     params = {"usertoken_str": "c341eda1-cd8d-48ae-bbc4-c668de8f59","forum_id":"1","forum_title":"这是要修改的帖子","forum_desp":"帖子没人看才改的"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST','/v1/forum/modifyforum/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
