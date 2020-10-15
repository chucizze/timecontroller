from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args


class Forum(Base):
    __table_args__ = table_args
    __tablename__ = 'forum'
    forum_id = Column(Integer, primary_key=True)
    forum_title = Column(String(200))
    forum_publishtime = Column(String(20))
    forum_desp = Column(String(2000))
    forum_userinfoid = Column(Integer,ForeignKey('userinfo.userinfo_id'))
