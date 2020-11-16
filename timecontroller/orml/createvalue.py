from orml.dbbase import DBSession
from dbmodels.usermodel import User
from dbmodels.usertokenmodel import Usertoken
from dbmodels.userinfomodel import Userinfo
from dbmodels.picturemodel import Picture
from dbmodels.praisemodel import Praise
from dbmodels.commentmodel import Comment
from dbmodels.forummodel import Forum
from dbmodels.attentionmodel import Attention
from dbmodels.fansmodel import Fans


session = DBSession()

if session.query(User).count() == 0:
    userlist = [User(user_id=1, user_name="小红", user_password="abcdef", user_question="我多少岁", user_answer="18"),
                User(user_id=2, user_name="小明", user_password="123456", user_question="我来自哪里", user_answer="贵阳"),
                User(user_id=3, user_name="小蓝", user_password="67890", user_question="我读哪个大学", user_answer="贵大"),
                User(user_id=4, user_name="小绿", user_password="098765", user_question="杜鹃花是什么颜色", user_answer="红色"),
                User(user_id=5, user_name="小黄", user_password="567123", user_question="现在是几点",user_answer="起点")]
    for i in userlist:
        session.add(i)

if session.query(Userinfo).count() == 0:
    userinfolist = [Userinfo(userinfo_id=1,  userinfo_img="timer.jgp", userinfo_userid=1, userinfo_attentionnum=1,userinfo_fansnum=1),
                    Userinfo(userinfo_id=2,  userinfo_img="timer.jgp",  userinfo_userid=2,userinfo_attentionnum=2,userinfo_fansnum=1),
                    Userinfo(userinfo_id=3,  userinfo_img="timer.jgp", userinfo_userid=3,userinfo_attentionnum=3,userinfo_fansnum=3),
                    Userinfo(userinfo_id=4,  userinfo_img="timer.jgp", userinfo_userid=4,userinfo_attentionnum=4,userinfo_fansnum=4),
                    Userinfo(userinfo_id=5,  userinfo_img="timer.jgp",  userinfo_userid=5,userinfo_attentionnum=5,userinfo_fansnum=5)]

    for i in userinfolist:
        session.add(i)
        
        
if session.query(Usertoken).count() == 0:
    usertokenlist = [Usertoken(usertoken_str = "c341eda1-cd8d-48ae-bbc4-c668de8f59fa", usertoken_userid = 1),
                    Usertoken(usertoken_str = "5d6d58ea-d7f7-41dd-80e3-ad14e799bb8e", usertoken_userid = 2),
                    Usertoken(usertoken_str = "333358ea-d7f7-41dd-80e3-ad14e799bb8e", usertoken_userid = 3),
                    Usertoken(usertoken_str = "444458ea-d7f7-41dd-80e3-ad14e799bb8e", usertoken_userid = 4),
                    Usertoken(usertoken_str = "555558ea-d7f7-41dd-80e3-ad14e799bb8e", usertoken_userid = 5)]
    for i in usertokenlist:
        session.add(i)
                
         
if session.query(Forum).count()==0:
    forumlist = [
        Forum(forum_id=1, forum_title="每天坚持背单词", forum_desp="坚持就是胜利",forum_publishtime="2020-02-09 15:35:03", forum_userinfoid=1),
        Forum(forum_id=2, forum_title="每天要坚持跑三公里", forum_desp="自律给我自由",forum_publishtime="2020-09-09 15:35:03", forum_userinfoid=2),
        Forum(forum_id=3, forum_title="这个月要爬山一次",  forum_desp="一览众山小",forum_publishtime="2020-05-09 15:35:03", forum_userinfoid=5),
        Forum(forum_id=4, forum_title="大学参加一次马拉松",  forum_desp="最会跑步的最会写作",forum_publishtime="2020-06-09 15:35:03", forum_userinfoid=4)]
    for i in forumlist:
        session.add(i)
     
 
if session.query(Comment).count() ==0:
    commentlist = [
        Comment(comment_id=1, comment_content="今天天气真好", comment_time="2020-09-20 17:03:12", comment_userinfoid=1,comment_forumid=1),
        Comment(comment_id=2, comment_content="溪流的水真清", comment_time="2020-04-09 15:35:03", comment_userinfoid=2,comment_forumid=2),
        Comment(comment_id=3, comment_content="树叶真好看", comment_time="2020-07-09 16:35:03", comment_userinfoid=2,comment_forumid=3),
        Comment(comment_id=4, comment_content="这棵树真大", comment_time="2020-10-09 05:35:33", comment_userinfoid=2,comment_forumid=1),
        Comment(comment_id=5, comment_content="天上的云白白的", comment_time="2020-11-09 15:35:03", comment_userinfoid=3,comment_forumid=2),
        Comment(comment_id=6, comment_content="这家店好吃", comment_time="2019-12-09 09:23:08", comment_userinfoid=4,comment_forumid=3),
        Comment(comment_id=7, comment_content="我要减肥", comment_time="2020-11-27 03:35:03", comment_userinfoid=4,comment_forumid=2)]
    for i in commentlist:
        session.add(i)


if session.query(Praise).count() ==0:
    praiselist = [Praise(praise_id =1, praise_number = "100",praise_forumid =1,praise_userid=1),
                    Praise(praise_id =2, praise_number = "200",praise_forumid =2,praise_userid=2),
                    Praise(praise_id =3, praise_number = "300",praise_forumid =3,praise_userid=3),
                    Praise(praise_id =4, praise_number = "400",praise_forumid =4,praise_userid=4),
                    # Praise(praise_id =5, praise_number = "600",praise_forumid =5,praise_userid=5),
                    # Praise(praise_id =6, praise_number = "500",praise_forumid =6,praise_userid=6),
                  ]
    for i in praiselist:
        session.add(i)       




if session.query(Attention).count() == 0:
    attentionlist = [Attention(attention_id =1,attention_userid =1,attention_fansid=2),
                     Attention(attention_id =2,attention_userid =2,attention_fansid=3),
                     Attention(attention_id =3,attention_userid =1,attention_fansid=4),
                     Attention(attention_id =4,attention_userid =2,attention_fansid=1),
                     Attention(attention_id =5, attention_userid =2,attention_fansid=3),
                     Attention(attention_id =6, attention_userid =2,attention_fansid=4),
                     Attention(attention_id =7, attention_userid =3,attention_fansid=1),
                     Attention(attention_id =8, attention_userid =3,attention_fansid=2),
                     Attention(attention_id =9, attention_userid =3,attention_fansid=4),]
    for i in attentionlist:
        session.add(i)       

if session.query(Fans).count() == 0:
    fanslist = [Fans(fans_id=1, fans_name="小黄", fans_img="timer.jgp", fans_userid=1),
                Fans(fans_id=2, fans_name="小绿", fans_img="timer.jgp", fans_userid=5),
                Fans(fans_id=3, fans_name="小蓝", fans_img="timer.jgp", fans_userid=5),
                Fans(fans_id=4, fans_name="小明", fans_img="timer.jgp", fans_userid=5),
                     ]
    for i in fanslist:
        session.add(i)

session.commit()
session.close()                
                
                
                

