from orml.dbbase import DBSession
from dbmodels.usertokenmodel import Usertoken
from dbmodels.usermodel import User
from dbmodels.picturemodel import Picture
from dbmodels.praisemodel import Praise
from dbmodels.userinfomodel import Userinfo
from dbmodels.commentmodel import Comment
from dbmodels.forummodel import Forum
from dbmodels.attentionmodel import Attention
from sqlalchemy import desc
import uuid
import time

class Centerorml:
    def personalcencer(self,usertokenstr):
    
        session = DBSession()
        try:
            if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).count() > 0:
                userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
                
                 
                lista = session.query(Userinfo.userinfo_img,Userinfo.userinfo_name,).filter_by(userinfo_userid=userid[0]).all()

                listb = []                                
                for i in lista:
                     
                    item = {}
                    item["userinfo_img"] = i[0]
                    item["userinfo_name"] = i[1]
                    attentionnum = session.query(Attention).filter_by(attention_fansid=userid[0]).count()
                    item["userinfo_attentionnum"] = attentionnum
                    fansnum = session.query(Attention).filter_by(attention_userid=userid[0]).count()
                    item["userinfo_fansnum"] = fansnum
                    listb.append(item)
                return listb
        except Exception as a:
            print(a)
            return "False"

    def ownattention(self,usertokenstr):#查看我的关注
    
        session = DBSession()
        try:
            if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).count() > 0:
                userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
                attentionid = session.query(Attention.attention_userid).filter_by(attention_fansid=userid[0]).all()#查找出所有的关注用户id
                listb = []
                for j in attentionid:
                    lista = session.query(Userinfo.userinfo_img,Userinfo.userinfo_name,).filter_by(userinfo_userid=j[0]).all()

                    print(lista)                                 
                    for i in lista:
                     
                        item = {}
                        item["userinfo_img"] = i[0]
                        item["userinfo_name"] = i[1]
                   
                    listb.append(item)
                return listb
        except Exception as a:
            print(a)
            return "False"

    def cancleattention(self,usertokenstr,userid):		#取消关注
        session = DBSession() 			
        try:
            userid1 = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
            session.query(Attention).filter(Attention.attention_userid==userid,Attention.attention_fansid==userid1[0]).delete()
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return False

    def addattention(self,usertokenstr,userid):		#增加关注
        session = DBSession() 			
        try:
            userid1 = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
            session.add(Attention(attention_userid=userid,attention_fansid=userid1[0]))
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return False  

    def ownfans(self,usertokenstr):
    
        session = DBSession()
        try:
            if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).count() > 0:
                userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
                fansid = session.query(Attention.attention_fansid).filter_by(attention_userid=userid[0]).all()#查找出所有的fans用户id
                listb = []
                for j in fansid:
                    lista = session.query(Userinfo.userinfo_img,Userinfo.userinfo_name,).filter_by(userinfo_userid=j[0]).all()

                    print(lista)                                 
                    for i in lista:
                     
                        item = {}
                        item["userinfo_img"] = i[0]
                        item["userinfo_name"] = i[1]
                     
                   
                    listb.append(item)
                return listb
        except Exception as a:
            print(a)
            return "False"

    def showotherinfo(self,usertokenstr,userid):
    
        session = DBSession()#显示他人信息
        try:
            if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).count() > 0:
                
                lista = session.query(Userinfo.userinfo_img,Userinfo.userinfo_name,).filter_by(userinfo_userid=userid).all()

                listb = []
                print(lista)                                 
                for i in lista:
                     
                    item = {}
                    item["userinfo_img"] = i[0]
                    item["userinfo_name"] = i[1]
                   
                    attentionnum = session.query(Attention).filter_by(attention_fansid=userid).count()
                    item["userinfo_attentionnum"] = attentionnum
                    fansnum = session.query(Attention).filter_by(attention_userid=userid).count()
                    item["userinfo_fansnum"] = fansnum
                    listb.append(item)
                return listb
        except Exception as a:
            print(a)
            return "False"
            

