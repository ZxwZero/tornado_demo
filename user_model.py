from settings import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

 
class User(Base):
      __tablename__ = 'user'  
      id = Column(Integer, autoincrement=True, primary_key=True)
      user_name = Column(String(20))
      password = Column(String(20))
      create_time = Column(DateTime, default=datetime.now())
      is_login = Column(Boolean, default=False, nullable=False)
 
if __name__ == '__main__':
     Base.metadata.create_all() 