from flask_restful import Resource, Api
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.centerorml import Centerorml


class Personalcencer(Resource):

    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")

        co = Centerorml()
        temp = co.personalcencer(usertokenstr)
        if temp == "False":
            return jsonify(Info(False, '数据库错误', None).tojson())
        else:
            return jsonify(Info(True, temp, None).tojson())


class Ownattention(Resource):

    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")

        co = Centerorml()
        temp = co.ownattention(usertokenstr)
        if temp == "False":
            return jsonify(Info(False, '数据库错误', None).tojson())
        else:
            return jsonify(Info(True, temp, None).tojson())


class CancleAttention(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        userid = request.form["user_id"]
        co = Centerorml()
        temp = co.cancleattention(usertoken, userid)
        if temp:
            return jsonify(Info(True, "取消关注成功", None).tojson())
        else:
            return jsonify(Info(False, "数据库错误", None).tojson())


class AddAttention(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        userid = request.form["user_id"]
        print("$$$$$$$$$$$$$$$$", userid)
        co = Centerorml()
        temp = co.addattention(usertoken, userid)
        if temp:
            return jsonify(Info(True, "关注成功", None).tojson())
        else:
            return jsonify(Info(False, "数据库错误", None).tojson())


class OwnFans(Resource):

    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")
        print("@@@@@@@@@@@@@@@@@2", usertokenstr)
        co = Centerorml()
        temp = co.ownfans(usertokenstr)
        if temp == "False":
            return jsonify(Info(False, '数据库错误', None).tojson())
        else:
            return jsonify(Info(True, temp, None).tojson())


class Showotherinfo(Resource):
    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")
        userid = request.args.get("userid")
        co = Centerorml()
        temp = co.showotherinfo(usertokenstr, userid)
        if temp == "False":
            return jsonify(Info(False, '数据库错误', None).tojson())
        else:
            return jsonify(Info(True, temp, None).tojson())




