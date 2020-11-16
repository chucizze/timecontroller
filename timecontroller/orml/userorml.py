from orml.dbbase import DBSession
from dbmodels.usermodel import User
from dbmodels.userinfomodel import Userinfo
from dbmodels.usertokenmodel import Usertoken
import uuid


class Userorml:


    def checkuserexist(self, username):
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username).count() > 0:
                return True
        except Exception as a:
            print(a)
            return "False"
        else:
            return False

    def adduser(self, username, userpassword, userquestion, useranswer):

        session = DBSession()
        try:
            if username != "" and not self.checkuserexist(username):
                session.add(User(user_name=username,
                                 user_password=userpassword,
                                 user_question=userquestion,
                                 user_answer=useranswer))
                session.commit()
                session.close()  # 数据库表连接后，操作后，要关闭
                session = DBSession()
                userid = session.query(User.user_id).filter_by(user_name=username).one()

                session.add(Userinfo(userinfo_userid=userid[0]))  # 通过userid链接两个表
                session.commit()
                session.close()
                return True
            else:
                return False
        except Exception as a:
            print(a)
            # else:
            #     return False

    def userlogin(self, username, userpassword):  # 通过账号密码登录
        session = DBSession()
        try:
            if session.query(User).filter_by(user_name=username, user_password=userpassword).count() > 0:
                return True
        except Exception as a:
            print(a)
            return "False"
        else:
            return False

    def getidbyname(self, username):
        session = DBSession()
        try:
            userid = session.query(User.user_id).filter_by(user_name=username).one()
            return userid[0]
        except Exception as a:
            print(a)
        # else:
        #     return False

    def usertokenadd (self, username):
            session = DBSession()
            try:
             usertoken = str(uuid.uuid4())
             print(usertoken)
             a = Userorml()
             userid = a.getidbyname(username)
             print(userid)
             session.add(Usertoken(usertoken_str=usertoken, usertoken_userid=userid))
             session.commit()
             session.close()
             return usertoken
            except Exception as a:
                print(a)
                return "False"
            # else:
            #     return False

    def tokendelete(self, usertoken):
        session = DBSession()
        try:
            session.query(Usertoken).filter_by(usertoken_str=usertoken).delete()
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return False

    def getuserid(self, username):
        session = DBSession()
        try:
            userid = session.query(User.user_id).filter_by(user_name=username).all()
            item = {}
            item["user_id"] = userid[0]  # .decode("utf-8")
            return item
        except Exception as a:
            print(a)
            return False

    def judgeanswer(self, username, userquestion1, useranswer1):
        session = DBSession()
        try:
            print("$$$$$$$$$$$$$$$$$$$$$$4", userquestion1)
            print("%%%%%%%%%%%%%%%%%5", useranswer1)
            if session.query(User).filter_by(user_name=username, user_question=userquestion1).count() > 0:
                print("$$$$$$$$$$$$$$$$$$$$$$4", useranswer1)
                if session.query(User).filter_by(user_name=username, user_answer=useranswer1).count() > 0:
                    return 3
                return 1
            return 2
        except Exception as a:
            print(a)
            return "False"

    def changepassword(self, userid, usernewpassword):
        session = DBSession()
        try:
            session.query(User).filter_by(user_id=userid).update({'user_password': usernewpassword})
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return False

    def getidbytoken(self, usertokenstr):  # 重要
        session = DBSession()
        try:
            userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
            return userid[0]
        except Exception as a:
            print(a)

    def modifypassword(self, usertokenstr, usernewpassword):
        session = DBSession()
        a = Userorml()
        try:
            userid = a.getidbytoken(usertokenstr)
            session.query(User).filter_by(user_id=userid).update({'user_password': usernewpassword})
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return "False"

    def modifyquestion(self, usertokenstr, usernewquestion, usernewanswer):
        session = DBSession()
        a = Userorml()
        try:
            userid = a.getidbytoken(usertokenstr)
            print(2222222222222)
            print(userid)
            session.query(User).filter_by(user_id=userid).update(
                {'user_question': usernewquestion, 'user_answer': usernewanswer})

            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return "False"
        # else:
        #     return False