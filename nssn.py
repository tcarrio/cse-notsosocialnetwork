import bottle
import bottle_session
from bottle import route, run
from bottle import get, post, request
from bottle import static_file
from bottle import redirect
from bottle import HTTPError
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import hashlib, datetime


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:nssntest@localhost/nssndb",echo=True)
app = bottle.Bottle()
sqlPlugin = sqlalchemy.Plugin(engine,Base.metadata,create=True)
app.install(sqlPlugin)
#seshPlugin = bottle_session.SessionPlugin(cookie_lifetime=600)
#app.install(seshPlugin)
create_session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True)
    user_first_name = Column(String)
    user_last_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_dob = Column(DateTime)
    user_gender = Column(Boolean)
    
    def __init__(self, fname, lname, email, password, dob, gender):
        self.user_first_name = fname
        self.user_last_name = lname
        self.user_email = email
        self.user_password = password
        self.user_dob = dob
        self.user_gender = gender
        
    def is_legit(self):
        if isinstance(self.user_first_name,str) and \
            isinstance(self.user_last_name,str) and \
            isinstance(self.user_email,str) and \
            isinstance(self.user_password,str) and \
            isinstance(self.user_dob,datetime) and \
            isinstance(self.user_gender,boolean):
                return True
        else:
            return False
        

root_folder = '/home/tom/nssn'

# main redirect
@app.route('/')
def index():
    redirect('/index.html')

@app.route('/index.html')
def index():
    return static_file('index.html', root=root_folder+'/templates')

@app.route('/contacts.html')
def index():
    return static_file('contacts.html', root=root_folder+'/templates')

@app.route('/register.html')
def index():
    return static_file('register.html', root=root_folder+'/templates')

@app.route('/aboutus.html')
def index():
    return static_file('aboutus.html', root=root_folder+'/templates')

@app.post('/register')
def register_user(): 
    fname = request.forms.get("FName")
    lname = request.forms.get("LName")
    email = request.forms.get("Email")
    password = request.forms.get("Password")
    dobm = request.forms.get("DOBMonth")
    dobd = request.forms.get("DOBDay")
    doby = request.forms.get("DOBYear")
    gender = request.forms.get("gender")
    
    if not(fname and lname and email and password and dobm and dobd and doby and gender):
        return static_file('register.html',root=root_folder+'/templates')
    
    bGender = bool(gender=="male")
    dob = datetime.datetime.strptime("{}/{}/{}".format(dobd,dobm,doby), "%d/%m/%Y")
    hash = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
    new_user = User(fname,lname,email,hash,dob,bGender)
    
    session=create_session()
    session.add(new_user)
    session.commit()
    
    redirect('/index.html')
    
@app.post('/login')
def login_user():
    # get parameters from POST
    # process login info against db
    email = request.forms.get("Email")
    password = request.forms.get("Password")
    
    session = create_session()
    result = session.query(User).filter(User.user_email==email).first()

    print(email)
    print(password)
    if email and password:
        hash = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
        
        if result.user_email == email:
            if result.user_password == hash:
                redirect('/contacts.html')
        else:
            redirect('/index.html')
    
    return static_file('index.html', root=root_folder+'/templates')
    
# ASSET RETRIEVAL PATHS
@app.route('/js/<filename:path>')
def get_js(filename):
    return static_file(filename, root=root_folder+'/js')
@app.route('/css/<filename:path>')
def get_css(filename):
    return static_file(filename, root=root_folder+'/css')
@app.route('/img/avatars/<filename:path>')
def get_avatar(filename):
    return static_file(filename, root=root_folder+'/img/avatars')
@app.route('/img/background/<filename:path>')
def get_bg(filename):
    return static_file(filename, root=root_folder+'/img/background')
##


app.run(host='localhost',port=8080)