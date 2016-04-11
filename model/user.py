from sqlalchemy import Column, Integer, Sequence, String, DateTime, Boolean
from model.database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True)
    user_first_name = Column(String)
    user_last_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_dob = Column(DateTime)
    user_gender = Column(Boolean)
    
    def __init__(self,fname=None,lname=None,email=None,password=None,\
                 dob=None,gender=None,auth=False,active=False,id=None):
        
        self.auth=auth
        self.active=active
        self.user_id=id
        self.id=str(id)
        self.user_first_name = fname
        self.user_last_name = lname
        self.user_email = email
        self.user_password = password
        self.user_dob = dob
        self.user_gender = gender
        
    def is_authenticated(self):
        return self.auth
    def is_active(self):
        return self.active
    def is_anonymous():
        if not (self.auth or self.active):
            return True
        return False            
    def get_id(self):
        if not is_anonymous():
            return self.id
        else:
            return None
        
    def validate(self):
        if isinstance(self.user_first_name,str) and \
            isinstance(self.user_last_name,str) and \
            isinstance(self.user_email,str) and \
            isinstance(self.user_password,str) and \
            isinstance(self.user_dob,datetime) and \
            isinstance(self.user_gender,boolean):
                return True
        else:
            return False