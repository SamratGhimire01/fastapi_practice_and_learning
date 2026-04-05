from database import Base
from sqlalchemy import Column,Integer,String

class StudentDB(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    year = Column(Integer)
    email = Column(String(100))