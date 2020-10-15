#注意这里必须先引入model
from dbmodels.usermodel import User
from dbmodels.usertokenmodel import Usertoken
from dbmodels.userinfomodel import Userinfo
from dbmodels.picturemodel import Picture
from dbmodels.praisemodel import Praise
from dbmodels.commentmodel import Comment
from dbmodels.forummodel import Forum
from dbmodels.attentionmodel import Attention
from dbmodels.fansmodel import Fans
from orml.dbbase import engine
from orml.dbbase import Base
from orml.dbbase import DBSession
Base.metadata.create_all(engine)

import orml.createvalue
session = DBSession()
