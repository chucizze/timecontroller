from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args
class Attention(Base):
    __table_args__ = table_args
    __tablename__ = 'attention'
    attention_id = Column(Integer, primary_key=True)
    attention_userid=Column(Integer,ForeignKey('userinfo.userinfo_id'))
    attention_fansid=Column(Integer,ForeignKey('userinfo.userinfo_id'))