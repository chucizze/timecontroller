from orml.dbbase import DBSession
from dbmodels.usertokenmodel import Usertoken
from dbmodels.usermodel import User
from dbmodels.picturemodel import Picture
from dbmodels.praisemodel import Praise
from dbmodels.userinfomodel import Userinfo
from dbmodels.commentmodel import Comment
from dbmodels.forummodel import Forum
from sqlalchemy import desc
import uuid
import time


class Forumorml:                 
    def Forumshowme(self,usertokenstr):  #显示我的帖子
       
        session = DBSession()
        try:
            if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).count() > 0:
                userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertokenstr).one()
                userinfoid =session.query(Userinfo.userinfo_id).filter_by(userinfo_userid=userid[0]).one()
                lista = session.query(Forum.forum_id, Forum.forum_title, Forum.forum_publishtime,Forum.forum_userinfoid).filter_by(forum_userinfoid=userinfoid[0]).all()
                listb = []
                print(lista)                                 
                for i in lista:
                     
                    item = {}
                    forumpromulgator = session.query(Userinfo.userinfo_name).filter_by(userinfo_id=i[4]).one()
                    item["forum_promulgator"] = forumpromulgator[0]
                    item["forum_id"] = i[0]
                    item["forum_title"] = i[1]
                    item["forum_publishtime"] = i[2]
                    praisenum = session.query(Praise).filter_by(praise_forumid=i[0]).count()
                    item["praise_number"] = praisenum
                    listb.append(item)
                listb.sort(key = lambda x:x["forum_publishtime"], reverse = True) 
                return listb
        except Exception as a:
            print(a)
            return "False"   
            
            
    def forumcommentpublish(self,usertoken,forumid,commentcontent):#发布帖子的评论
        session = DBSession()
        try:
            userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertoken).one()
            userinfoid = session.query(Userinfo.userinfo_id).filter_by(userinfo_userid=userid[0]).one()
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            session.add(Comment(comment_forumid=forumid,
                                comment_userinfoid=userinfoid[0],
                                comment_content=commentcontent,
                                comment_time=nowtime))
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return "False"              
            
    

    def publishforum(self,usertoken,forumtitle,forumdesp):
        session = DBSession()
        try:
            userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertoken).one()
            userinfoid = session.query(Userinfo.userinfo_id).filter_by(userinfo_userid=userid[0]).one()
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            session.add(Forum(forum_userinfoid=userinfoid[0],
                              forum_title=forumtitle,
                              forum_publishtime=nowtime,
                              forum_desp=forumdesp))
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
            return "False"


    def forumallshow(self,usertoken,forumid):
        session = DBSession()
        if session.query(Usertoken.usertoken_userid).filter_by(usertoken_str = usertoken).count()>0:
           
           try:
           
               userinfoid = session.query(Forum.forum_userinfoid).filter_by(forum_id=forumid).one()
               userinfoimg = session.query(Userinfo.userinfo_img).filter_by(userinfo_id = userinfoid[0]).one()
               userinfoname = session.query(Userinfo.userinfo_name).filter_by(userinfo_id = userinfoid[0]).one() 
               item = {}
               lista = []
               lista = session.query(Forum.forum_id,Forum.forum_title,Forum.forum_publishtime,Forum.forum_desp).filter_by(forum_id=forumid).all() 
               for i in lista:
                   item["forum_id"] = i[0]
                   item["forum_userimg"] = userinfoimg[0]
                   item["forum_username"] = userinfoname[0]
                   item["forum_title"] = i[1]
                   item["forum_publishtime"] = i[2]
                   item["forum_desp"] = i[3]
                   praisenum = session.query(Praise).filter_by(praise_forumid=forumid).count()
                   item["praise_number"] = praisenum
           
               listc = session.query(Comment.comment_id,Comment.comment_content,Comment.comment_time,Comment.comment_userinfoid).filter_by(comment_forumid = forumid).all()
               commentlist = []
               for j in listc:
                   comer = {} 
                   comer["comment_id"] = j[0]
                   name = session.query(Userinfo.userinfo_name).filter_by(userinfo_id=j[3]).one()
                   comer["comment_name"] = name[0]
                   img = session.query(Userinfo.userinfo_img).filter_by(userinfo_id=j[3]).one()
                   comer["comment_userimg"] = img[0]
                   comer["comment_content"] = j[1]
                   comer["comment_time"] = j[2]
                   commentlist.append(comer)
               commentlist.sort(key = lambda x : x['comment_time'],reverse=False)
            #    item["book_comments"] = commentlist
            #    return item
           except Exception as a:
               print(a)
               return "False" 
         
    def forumpraise(self,usertoken,forumid,praisestatus):
        session = DBSession()
        try:
            userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertoken).one()
            if int(praisestatus) == 1 and session.query(Forum).filter_by(forum_id = forumid).count()>0:
                session.query(Praise).filter_by(praise_forumid = forumid, praise_userid = userid[0]).delete()
                session.commit()
                session.close()
                return "0"
            elif int(praisestatus) == 0:
                if session.query(Praise).filter_by(praise_forumid =forumid,praise_userid = userid[0]).count()>0:
                    return "False"
                else:
                    nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
                    session.add(Praise(praise_forumid = forumid, praise_userid = userid[0]))
                    session.commit()
                    session.close()
                    return "1"
            else:
                return "False"
        except Exception as a:
            print(a)
            return "False"  
    
    


    def modifyforum(self,usertoken,forumid,forumtitle,forumdesp):
    
        session = DBSession()  #bookclass表
        try:
            #userid = session.query(Usertoken.usertoken_userid).filter_by(usertoken_str=usertoken).one()会出现访问不到的错误
            #print("$$$$$$$$$$$$$$$",userid)
            #usercollege = session.query(Userinfo.userinfo_college).filter_by(userinfo_userid=userid[0]).one()
            #print("&&&&&&&&&&&&&&&",usercollege[0])
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            session.query(Forum).filter_by(forum_id=forumid).update({"forum_title":forumtitle,
             "forum_desp":forumdesp,
             "forum_publishtime":nowtime,  
             })
            session.commit()
            session.close()
            return True
        except Exception as a:
            print(a)
    
    
    
    def delectforum(self,usertokenstr,forumid):
       
        session = DBSession()			
        try:
            session.query(Forum).filter_by(forum_id=forumid).delete()
            session.commit()
            session.close() 
            return True
        except Exception as a:
            print(a)
            return False
    
    
    
    
    
    
    
            
            
                                
