from flask_restful import Resource,Api
from flask import request
from flask import jsonify
from flask import Response
from tools.info import Info
from conf import httpserver, httpport
from tools.crossdomain import allow_cross_domain
from orml.forumorml import Forumorml


class ForumDefshow(Resource):

    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")
        fo = Forumorml()
        temp = fo.forumdefshow(usertokenstr)
        if temp == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        else:
            return jsonify(Info(True,temp,None).tojson())


class Forumshowme(Resource):

    @allow_cross_domain
    def get(self):
        usertokenstr = request.args.get("usertoken_str")
        fo = Forumorml()
        temp = fo.Forumshowme(usertokenstr)
        if temp == "False":
            return jsonify(Info(False,'数据库错误',None).tojson())
        else:
            return jsonify(Info(True,temp,None).tojson())


class ForumCommentPublish(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        forumid = request.form["forum_id"]
        commentcontext = request.form["comment_context"]
        fo = Forumorml()
        temp = fo.forumcommentpublish(usertoken,forumid,commentcontext)
        if temp:
            return jsonify(Info(True,"发布成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())


class PublishForum(Resource):
    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        forumtitle = request.form["forum_title"]
        forumdesp = request.form["forum_desp"]
        fo = Forumorml()
        temp = fo.publishforum(usertoken,forumtitle,forumdesp)
        if temp:
            return jsonify(Info(True,"发布成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())

            
class Forumallshow(Resource):
     @allow_cross_domain
     def get(self):
         usertoken = request.args.get("usertoken_str")
         forumid = request.args.get("forum_id")
         fo = Forumorml()
         temp = fo.forumallshow(usertoken,forumid)
         if temp == False:
             return jsonify(Info(False,"数据库错误",None).tojson())
         else:
             return jsonify(Info(True,"返回成功",temp,None).tojson())


class  Forumpraise(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        forumid = request.form["forum_id"]
        praisestatus = request.form["praise_status"]
        fo = Forumorml()
        temp = fo.forumpraise(usertoken,forumid,praisestatus)
        if temp == "False":
            return jsonify(Info(False,'数据库错误').tojson())
        elif temp == "0":
            return jsonify(Info(True,"取消点赞",None).tojson())
        else:
            return jsonify(Info(True,"点赞成功",None).tojson())


class ModifyForum(Resource):
    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        forumid = request.form["forum_id"]
        forumtitle = request.form["forum_title"]
        forumdesp = request.form["forum_desp"]
        fo = Forumorml()
        temp = fo.modifyforum(usertoken,forumid,forumtitle,forumdesp)
        if temp:
            return jsonify(Info(True,"帖子修改成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())


class DeleteForum(Resource):

    @allow_cross_domain
    def post(self):
        usertoken = request.form["usertoken_str"]
        forumid = request.form["forum_id"]
        fo = Forumorml()
        temp = fo.delectforum(usertoken,forumid)
        if temp:
            return jsonify(Info(True,"帖子删除成功",None).tojson())
        else:
            return jsonify(Info(False,"数据库错误",None).tojson())
