import unittest
import json
import http.client as httplib
import urllib.parse as urllib
from conf import httpserver
from conf import httpport
import urllib

conn = httplib.HTTPConnection(httpserver, httpport)
header = {"Content-type": "application/x-www-form-urlencoded"}

class TestUser(unittest.TestCase):

 # def test_checkuserexist(self):
 #       global conn
 #       i = urllib.parse.quote("小熊")
 #       conn.request('GET', '/v1/user/signup/?user_name='+i)
 #       data = json.loads(conn.getresponse().read().decode("utf-8"))
 #       print(data)
 #       self.assertTrue(data["infostatus"])
 #   #
 #   def test_adduser1(self):
 #        global conn
 #        global header
 #        params = {"user_name": "小熊",
 #                  "user_password": "123",
 #                  "user_question": "我班主任姓名",
 #                  "user_answer": "老熊"}
 #        params = urllib.parse.urlencode(params)
 #        conn.request('POST', '/v1/user/signup/', params, header)
 #        data = json.loads(conn.getresponse().read().decode("utf-8"))
 #        print(data)
 #        self.assertFalse(data["infostatus"])

   def test_userlogin(self):
       global conn
       global header
       params = {"user_name": "小明",
                 "user_password": "123456"}
       params = urllib.parse.urlencode(params)
       conn.request('POST', '/v1/user/login/', params, header)
       data = json.loads(conn.getresponse().read().decode("utf-8"))
       # print(data)
       self.assertTrue(data["infostatus"])


   # def test_tokendelete(self):
   #     global conn
   #     global header
   #     params = {"usertoken_str": "9967b5c3-92a0-4224-8c68-5ee524d80134"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST', '/v1/token/delete/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])



    # def test_judgeanswer(self):
    #    global conn
    #    k = urllib.parse.quote("小熊")
    #    i = urllib.parse.quote("我班主任姓名")  #这句话的语法？
    #    j = urllib.parse.quote("老熊")
    #    conn.request('GET', '/v1/user/judgeanswer/?user_name='+k+'&user_question='+i+'&user_answer='+j)
    #    data = json.loads(conn.getresponse().read().decode("utf-8"))
    #    print(data)
    #    self.assertTrue(data["infostatus"])


   # def test_changepassword(self):
   #     global conn
   #     global header
   #     params = {"user_id": "1",
   #               "user_password": "abcde"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST','v1/user/changepwd/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])
#
   # def test_modifypassword(self):
   #     global conn
   #     global header
   #     params = {"usertoken_str": "c341eda1-cd8d-48ae-bbc4-c668de8f59fa",
   #               "user_newpassword": "abcde"}
   #     params = urllib.parse.urlencode(params)
   #     conn.request('POST', '/v1/modify/password/', params, header)
   #     data = json.loads(conn.getresponse().read().decode("utf-8"))
   #     print(data)
   #     self.assertTrue(data["infostatus"])

   def test_modifyquestion(self):
       global conn
       global header
       params = {"usertoken_str": "c341eda1-cd8d-48ae-bbc4-c668de8f59fa",
                 "user_question": "我高三班主任姓名",
                 "user_answer": "石老师"}
       params = urllib.parse.urlencode(params)
       conn.request('POST', '/v1/set/passquestion/', params, header)
       data = json.loads(conn.getresponse().read().decode("utf-8"))
       print(data)
       self.assertTrue(data["infostatus"])
