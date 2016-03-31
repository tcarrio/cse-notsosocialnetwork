from bottle import route, run
from bottle import static_file
from bottle import redirect

root_folder = '/home/tom/nssn'

# main redirect
@route('/')
def index():
    redirect('/index.html')

@route('/index.html')
def index():
    return static_file('index.html', root=root_folder+'/templates')

@route('/contacts.html')
def index():
    return static_file('contacts.html', root=root_folder+'/templates')

@route('/register.html')
def index():
    return static_file('register.html', root=root_folder+'/templates')

@route('/aboutus.html')
def index():
    return static_file('aboutus.html', root=root_folder+'/templates')

@post('/register')
def register_user():
    
    
#@route('/login')
#def login():
#    # get parameters from POST
#    # process login info against db
#    return static_file('index.html', root=root_folder+'/templates')
    
# ASSET RETRIEVAL PATHS
@route('/js/<filename:path>')
def get_js(filename):
    return static_file(filename, root=root_folder+'/js')
@route('/css/<filename:path>')
def get_css(filename):
    return static_file(filename, root=root_folder+'/css')
@route('/img/avatars/<filename:path>')
def get_avatar(filename):
    return static_file(filename, root=root_folder+'/img/avatars')
@route('/img/background/<filename:path>')
def get_bg(filename):
    return static_file(filename, root=root_folder+'/img/background')
##


run(host='localhost',port=8080)