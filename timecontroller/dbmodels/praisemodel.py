from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args
class Praise(Base):
    __table_args__ = table_args
    __tablename__ = 'praise'
    praise_id= Column(Integer, primary_key=True)
    praise_number=Column(String(20))
    praise_forumid=Column(Integer,ForeignKey('forum.forum_id'))
    praise_userid=Column(Integer,ForeignKey('userinfo.userinfo_id'))