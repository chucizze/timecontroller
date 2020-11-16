from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# engine = create_engine('mysql+mysqlconnector://root:jiangyu991213@0.0.0.0/timecontroller?use_unicode=1&charset=utf8', echo=True)
engine = create_engine("mysql://root:abcdefg@127.0.0.1/timecontroller?use_unicode=1&charset=utf8", echo=True)
DBSession = sessionmaker(bind=engine)


