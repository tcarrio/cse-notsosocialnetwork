from flask import Flask,render_template,redirect,url_for,request,session,escape
from model.database import Account,Profile,Post,Message,db_session
from sqlalchemy import *
from sqlalchemy.exc import *
import datetime, hashlib
#from flask import json,jsonify

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config.env_config.ProductionConfig')

db = create_engine(app.config['DATABASE_URI'])


### ROOT REQUEST
@app.route('/',methods=['GET'])
def root_page():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('frontpage'))
    
### FRONTPAGE
@app.route('/frontpage',methods=['GET'])
def frontpage():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('index.html')

### HOMEPAGE
@app.route('/home',methods=['GET'])
def home():
    if 'user' not in session:
        return redirect(url_for('frontpage'))
    print('home was accessed')
    return render_template('home.html')

### CONTACT
@app.route('/contacts',methods=['GET'])
def contacts():
    return render_template('contacts.html')

### REGISTRATION
@app.route('/registration',methods=['GET'])
def registration():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('register.html')

### ABOUT US
@app.route('/aboutus',methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

### PROFILE
@app.route('/profile', methods=['GET'])
def profile():
    if 'user' not in session:
        return redirect(url_for('register'))
    result = db_session.query(Account).filter(Account.account_email==session['user']).first()
    return render_template('profile.html')
    
### LOGIN 
@app.route('/login', methods=['POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
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
    
### REGISTER
@app.route('/register', methods=['POST'])
def register(): 
    if 'user' in session:
        return redirect(url_for('home'))
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
        # entry exists, fail back to registration
        return redirect(url_for('registration'))
        
    session['user'] = email
    return redirect(url_for('frontpage'))
    
### SEARCH
@app.route('/search', methods=['GET'])
def search():
    print(request.args) #dict
    return

### LOGOUT
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('frontpage'))
    
if __name__=="__main__":
    app.run(host=app.config['EXT_IP'],port=80,debug=True)
