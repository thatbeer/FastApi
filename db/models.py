from tokenize import String
from db.database import Base
from sqlalchemy.sql.sqltypes import Integer , String , Float
from sqlalchemy import Column

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    enail = Column(String)
    pasword = Column(String)