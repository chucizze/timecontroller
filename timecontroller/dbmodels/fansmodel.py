from sqlalchemy import Column, String, Integer,ForeignKey
from orml.dbbase import Base
from conf import table_args

class Fans(Base):
    __table_args__ = table_args
    __tablename__ = 'fans'
    fans_id=Column(Integer, primary_key=True)
    fans_name=Column(String(20))
    fans_img=Column(String(100))
    fans_userid=Column(Integer,ForeignKey('userinfo.userinfo_id'))