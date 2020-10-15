from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args


class Userinfo(Base):
    __table_args__ = table_args
    __tablename__ = 'userinfo'
    userinfo_id = Column(Integer, primary_key=True)
    userinfo_img = Column(String(20))
    userinfo_userid= Column(Integer,ForeignKey('user.user_id'))
    userinfo_name = Column(String(100))
    userinfo_attentionnum=Column(Integer)
    userinfo_fansnum=Column(Integer)