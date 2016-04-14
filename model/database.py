from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, Boolean, ForeignKey
from config.env_config import ProductionConfig as Conf

engine = create_engine(Conf.DATABASE_URI, convert_unicode=True)


def get_new_session():
    return scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

db_session = get_new_session()

Base = declarative_base()
Base.query = db_session.query_property()

#SQL ORM Account Class
class Account(Base):
    __tablename__ = 'accounts'
    #account_id = Column(Integer,primary_key=True)
    account_first_name = Column(String(255))
    account_last_name = Column(String(255))
    account_email = Column(String(255),primary_key=True)
    account_password = Column(String(64))
    account_dob = Column(DateTime)
    account_gender = Column(Boolean)
    
    profile_rel = relationship("Profile")
    post_rel = relationship("Post")
    message_rel = relationship("Message")
    
    def __init__(self,fname=None,lname=None,email=None,password=None,\
                 dob=None,gender=None):
        
        self.account_first_name = fname
        self.account_last_name = lname
        self.account_email = email
        self.account_password = password
        self.account_dob = dob
        self.account_gender = gender
        
    def __repr__(self):
        return '<User {}>'.format(self.name)
        
#SQL ORM Profile Class                
class Profile(Base):
    __tablename__ = 'profiles'
    profile_id = Column(Integer,primary_key=True)
    profile_uri = Column(String(255))
    profile_about = Column(String(1023))
    account_email = Column(String(255),ForeignKey('accounts.account_email'))
    
    account_rel = relationship("Account",foreign_keys='accounts.account_email')
    
    def __init__(self,id=None,uri=None,about=None,email=None):
        self.profile_id = id;
        self.profile_uri = uri;
        self.profile_about = about;
        self.account_email = email;
        
    def __repr__(self):
        return '<Profile {}>'.format(self.name)
        
#SQL ORM Post Class
class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer,primary_key=True)
    post_uri = Column(String(255))
    account_email = Column(String(255),ForeignKey('accounts.account_email'))
    receiver_email = Column(String(255),ForeignKey('accounts.account_email'))
    post_date = Column(DateTime)
    post_content = Column(String(4096))
    
    account_rel = relationship("Account",foreign_keys='accounts.account_email')
    
    def __init__(self,id=None,uri=None,pFrom=None,pTo=None,pDate=None,pContent=None):
        self.post_id = id
        self.post_uri = uri
        self.account_email = pFrom
        self.receiver_email = pTo
        self.post_date = pDate
        self.post_content = pContent
        
    def __repr__(self):
        return '<Post {}>'.format(self.name)
            
#SQL ORM Message Class
class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer,primary_key=True)
    message_uri = Column(String(255))
    account_email = Column(String(255),ForeignKey('accounts.account_email'))
    receiver_email = Column(String(255),ForeignKey('accounts.account_email'))
    message_date = Column(DateTime)
    message_title = Column(String(255))
    message_content = Column(String(4096))
    
    account_rel = relationship("Account",foreign_keys='accounts.account_email')
    
    def __init__(self,mId=None,uri=None,mFrom=None,mTo=None,mDate=None,title=None,mContent=None):
        self.message_id = mId
        self.message_uri = uri
        self.account_email = mFrom
        self.receiver_email = mTo
        self.message_date = mDate
        self.message_title = title
        self.message_content = mContent
    
    def __repr__(self):
        return '<Message {}>'.format(self.name)
        
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import Account
    import Profile
    import Post
    import Message
    Base.metadata.create_all(bind=engine)