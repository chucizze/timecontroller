from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args


class Picture(Base):
    __table_args__ = table_args
    __tablename__ = 'picture'
    picture_id = Column(Integer, primary_key=True)
    picture_name = Column(String(100))
    picture_forumid = Column(Integer,ForeignKey('forum.forum_id'))



