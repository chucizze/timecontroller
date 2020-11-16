from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args
class Comment(Base):
    __table_args__ = table_args
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_content = Column(String(200))
    comment_time=Column(String(20))
    comment_userinfoid = Column(Integer,ForeignKey('userinfo.userinfo_id'))
    comment_forumid = Column(Integer,ForeignKey('forum.forum_id'))