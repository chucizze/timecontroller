from flask_restful import Resource,Api
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.userorml import Userorml


class CheckUserExist(Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        print("*"*50)
        print(username)
        uo = Userorml()
        name = uo.checkuserexist(username)
        if name == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        elif not name:
            return jsonify(Info(True,'可用的用户名',None).tojson())
        else:
            return jsonify(Info(False,'用户名已存在',None).tojson())


class AddUser(Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_name"]
        userpassword = request.form["user_password"]
        userquestion = request.form["user_question"]
        useranswer = request.form["user_answer"]
        print(username)
        uo = Userorml()
        temp = uo.adduser(username,userpassword,userquestion,useranswer)
        if temp:
            return jsonify(Info(True,"注册成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())


class UserLogin(Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_name"]
        userpassword = request.form["user_password"]
        print("*"*50)
        print(username)
        print(userpassword)
        uo = Userorml()
        temp = uo.userlogin(username,userpassword)
        usertoken = uo.usertokenadd(username)
        if temp:
            return jsonify(Info(True,"登陆成功",usertoken).tojson())
        elif temp == "False":
            return jsonify(Info(False,"数据库错误",None).tojson())
        else:
            return jsonify(Info(False,"用户名或密码错误",None).tojson())


class TokenDelete(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        uo = Userorml()
        temp = uo.tokendelete(usertoken)
        if temp:
            return jsonify(Info(True,"usertoken删除成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())


class JudgeAnswer(Resource):

    @allow_cross_domain
    def get(self):
        username = request.args.get("user_name")
        userques = request.args.get("user_question")
        useranswer = request.args.get("user_answer")
        print("$$$$$$$$$$$$$$$$$$$$$$4",username)
        uo = Userorml()
        temp = uo.judgeanswer(username,userques,useranswer)
        print("########################",temp)
        if temp==3:
            temp1 = uo.getuserid(username)
            if temp1:
                return jsonify(Info(True,"密保问题及答案正确",temp1).tojson())
            else:
                return jsonify(Info(False,'用户名错误',None).tojson())
        elif temp == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        elif temp == 1:
            return jsonify(Info(False,'密保答案输入错误',None).tojson())
        else:
            return jsonify(Info(False,'密保问题输入错误',None).tojson())


class ChangePassword(Resource):

    @allow_cross_domain
    def post(self):
        username = request.form["user_id"]
        userpassword = request.form["user_password"]
        uo = Userorml()
        temp = uo.changepassword(username,userpassword)
        if temp:
            return jsonify(Info(True,"密码修改成功",None).tojson())
        else:
            return jsonify(Info(False,'数据库错误',None).tojson())


class ModifyPassword(Resource):

    @allow_cross_domain
    def post(self):
        usertokenstr = request.form["usertoken_str"]
        usernewpassword = request.form["user_newpassword"]
        uo = Userorml()
        temp = uo.modifypassword(usertokenstr,usernewpassword)
        if temp:
            return jsonify(Info(True,"密码修改成功",None).tojson())
        else: 
            return jsonify(Info(False,'数据库错误',None).tojson())
#        else:
#            return jsonify(Info(False,'原密码输入错误',None).tojson())

class ModifyQuestion(Resource):
    @allow_cross_domain
    def post(self):
        usertokenstr = request.form["usertoken_str"]
        usernewquestion = request.form["user_question"]
        usernewanswer = request.form["user_answer"]
        uo = Userorml()
        temp = uo.modifyquestion(usertokenstr, usernewquestion, usernewanswer)
        if temp:
            return jsonify(Info(True, "设置成功", None).tojson())
        else:
            return jsonify(Info(False, '数据库错误', None).tojson())


