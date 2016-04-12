from flask import Flask,render_template,redirect,url_for,request,session,escape
from model.database import Account,Profile,Post,Message,db_session
from model.security import Hasher
from model.datetool import DateHelper
from sqlalchemy import *
from sqlalchemy.exc import *
import datetime, hashlib
#from flask import json,jsonify

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config.env_config.ProductionConfig')

db = create_engine(app.config['DATABASE_URI'])

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
                session['user']=result.user_email
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
    print('D:{}\tM:{}\tY:{}'.format(dobd,dobm,doby))
    dob = datetime.datetime.strptime("{}/{}/{}".format(dobd,dobm,doby), "%d/%m/%Y")
    print('About to hash password')
    hashedP = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
    print('Creating user')
    new_account = Account(fname,lname,email,hashedP,dob,bGender)
    print('Created user')
    
    try:
        db_session.add(new_account)
        db_session.commit()
    except IntegrityError:
        return redirect(url_for('registration'))
        
    
    print('About to flash')
    app.flash('You have successfully registered!')
    return redirect(url_for('home'))
    
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('frontpage'))
    
if __name__=="__main__":
    app.run(host='104.131.109.224',port=8080,debug=True)
