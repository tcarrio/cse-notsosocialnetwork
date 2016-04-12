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

    result = db_session.query(Account).filter(Account.account_email==email).first()
    if email and password:
        hash = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
        
        if result.account_email == email:
            if result.account_password == hash:
                session['user']=result.account_email
                return redirect(url_for('home'))
        else:
            return redirect('/index.html')
    
    return redirect(url_for('frontpage'))
    
@app.route('/register', methods=['POST'])
def register(): 
    fname = request.form['FName']
    lname = request.form['LName']
    email = request.form['Email']
    password = request.form['Password']
    dobm = request.form['DOBMonth']
    dobd = request.form['DOBDay']
    doby = request.form['DOBYear']
    gender = request.form['gender']
    
    if not(fname and lname and email and password and dobm and dobd and doby and gender):
        return redirect(url_for('registration'))
    
    bGender = bool(gender=="male")
    dob = datetime.datetime.strptime("{}/{}/{}".format(dobd,dobm,doby), "%d/%m/%Y")
    hashedP = hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]
    new_account = Account(fname,lname,email,hashedP,dob,bGender)
        
    try:
        db_session.add(new_account)
        db_session.commit()
    except IntegrityError:
        return redirect(url_for('registration'))
        
    session['user'] = email
    return redirect(url_for('frontpage'))
    
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('frontpage'))
    
if __name__=="__main__":
    app.run(host='104.131.109.224',port=80,debug=True)
