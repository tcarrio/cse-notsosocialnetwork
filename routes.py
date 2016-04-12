from flask import Flask,render_template,redirect,url_for,request
#from flask_login import LoginManager
from model.manager import login_manager
import flask.ext.login as flask_login
from model.user import User
from model.security import Hasher
from model.datetool import DateHelper
from sqlalchemy import *
#from flask import json,jsonify

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config.env_config.DevelopmentConfig')
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

db = create_engine(app.config['DATABASE_URI'])

user = User() # unauth user
dateFrm = DateHelper() # ;)
hshr = Hasher()

@app.route('/')
def root_page():
#    if(user.is_authenticated):
#        return redirect(url_for('home'))
#    else:
    return redirect(url_for('frontpage'))
    
@app.route('/frontpage')
def frontpage():
    return render_template('index.html')

@app.route('/home')
def home():
    print('home was accessed')
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/registration')
def registration():
    return render_template('register.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
    
@app.route('/login', methods=['POST'])
def login():
    email = request.form['Email']
    password = request.form['Password']
    
    session = create_session()
    result = session.query(User).filter(User.user_email==email).first()
    if email and password:
        hash = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
        
        if result.user_email == email:
            if result.user_password == hash:
                return redirect(url_for('home'))
        else:
            return redirect('/index.html')
    
    return redirect(url_for('frontpage'))
    
@app.route('/register', methods=['POST'])
def register(): 
    print('Entered register')
    fname = request.form['FName']
    lname = request.form['LName']
    email = request.form['Email']
    password = request.form['Password']
    dobm = request.form['DOBMonth']
    dobd = request.form['DOBDay']
    doby = request.form['DOBYear']
    gender = request.form['gender']
    print('Parsed form')
    
    if not(fname and lname and email and password and dobm and dobd and doby and gender):
        app.flash('Not all required information was received. Please try again')
        return redirect(url_for('registration'))
    
    bGender = bool(gender=="male")
    print('About to format date')
    dob = dateFrm.get_db_date(dobd,dobm,doby)
    print('About to hash password')
    hashedP = hshr.get_hash(password)
    print('Creating user')
    new_user = User(fname,lname,email,hashedP,dob,bGender)
    
#    session=create_session()
#    session.add(new_user)
#    session.commit()
    
    print('About to flash')
    app.flash('You have successfully registered!')
    return redirect(url_for('home'))
    
@app.route('/logout')
#@login_required
def logout():
    logout_user()
    
    
    
    
if __name__=="__main__":
    app.run()
