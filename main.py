from flask import Flask, render_template ,request , session , redirect ,flash , url_for ,escape
from functools import wraps
from flask_login import  UserMixin, login_required,login_manager,logout_user,login_user, current_user
import os , math
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists    
from sqlalchemy.orm.attributes import flag_modified
from socket import socket
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
from datetime import datetime
from datetime import date as d
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
        MAIL_SERVER = "smtp.gmail.com" , 
        MAIL_PORT = "465" , 
        MAIL_USE_SSL= True ,
        MAIL_USERNAME = params['gmail-user'],
        MAIL_PASSWORD = params['gmail-password'] )

mail = Mail(app)

# if (local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

# else:
#     app.config[''] = params['prod_uri']
SQLALCHEMY_DATABASE_URI = os.environ('postgres://fsfeflckrgjsho:a7873d567e5e2d6f84e6c1c611fe3038369d8011c319ff1c598b94a32f250ff3@ec2-54-163-97-228.compute-1.amazonaws.com:5432/davocbj77nd6gp')
db = SQLAlchemy(app)
a=0
class Contacts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    phone_num = db.Column(db.String(12),  nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20))
    email = db.Column(db.String(20),  nullable=False)

class Posts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    slug = db.Column(db.String(12),  nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(12))

    date = db.Column(db.String(12))
    img_file = db.Column(db.String(12))

    #email = db.Column(db.String(120),  nullable=False)

class Registration(db.Model):
    
    username = db.Column(db.String(80) , primary_key=True)
    name = db.Column(db.String(80) )
    email   = db.Column(db.String(80) , nullable=True)
    pasword = db.Column(db.String(80) , nullable = False)

def login_required(f):
    @wraps(f)
    def wrap():
        if a:
            return f()
        else:
            
            flash("You need to login first")
            return redirect('/login')

    return wrap
		

@app.route("/")
def index():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page')

    if (not str(page).isnumeric()):
        page =1
    page = int(page)

    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]


    if (page==1):
        prev = "#"
        next = "/?page=" + str(page+1)

    elif (page==last):
        prev = "/?page="  + str(page-1)
        next = "#"

    else:
        prev = "/?page=" + str(page -1)
        next = "/?page="  + str(page+1)

    return render_template('index.html' , params = params , posts = posts , prev = prev , next = next)

@app.route("/post/<string:post_slug>" , methods=['GET'])
def post_route(post_slug):

    post = Posts.query.filter_by(slug = post_slug).first()

    return render_template('post.html' , params = params , post= post )


@app.route("/dashboard" , methods=['GET' , 'POST'])
def dashboard():
    if ('user' in session and session['user']==params['admin_user']):
        posts = Posts.query.all()

        return render_template('dashboard.html' , params = params , posts = posts)

    if request.method=='POST':
        username  = request.form.get('uname')
        userpass  = request.form.get('pass')

        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html' , params = params , posts = posts)
        
        else:
            flash('Wrong Username or Password')
            return render_template('admin.html' , params= params)

    else:
        return render_template('admin.html' , params = params)


@app.route("/about")
def about():
    return render_template('about.html' , params = params)

@app.route("/editor")
def editor():
    return render_template('editor.html' , params = params)


@app.route("/practice")
def p():
    if session['logged_in']:
        return render_template('practice.html' , params = params)
    else:
        return redirect('/login')


@app.route("/edit/<string:sno>" , methods = ['GET' , 'POST'])
def edit(sno):
    if ('user' in session and session['user']==params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = d.today()


            if sno =="0":
                post = Posts(title = box_title , slug = slug , content = content , tagline = tline ,img_file = img_file , date = date)
                db.session.add(post)
                db.session.commit()
              
            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title  = box_title
                post.slug  = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/' + sno)
        
        post = Posts.query.filter_by(sno = sno).first()
        return render_template('edit.html' , params = params ,  sno= sno , post = post)
    else:
        
        return dashboard()



@app.route("/uploader" , methods = ['GET' , 'POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_user']):

        if(request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] , secure_filename(f.filename)))
            return "Uploaded Successfully!"

    

@app.route("/delete/<string:sno>" , methods = ['GET' , 'POST'])
def delete(sno):
    if ('user' in session and session['user']==params['admin_user']):
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')

@app.route("/contact" , methods = ['GET' , 'POST'])
def contact():
    if request.method=='POST':
  
        '''Add entry to DB'''
        name = request.form.get('name')
        email= request.form.get('email')
        phone  = request.form.get('phone')
        message= request.form.get('message')

        entry = Contacts(name=name , phone_num = phone , msg = message , date= d.today(), email = email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from learn2_cod' + name , 
                    sender = email ,
                    recipients = [params['gmail-user']] ,
                    body = message +  "\n"  + phone
                    )

    return render_template('contact.html' , params = params)


@app.route("/contact1" , methods = ['GET' , 'POST'])
def contact1():
    if request.method=='POST':
  
        '''Add entry to DB'''
        name = request.form.get('name')
        email= request.form.get('email')
        phone  = request.form.get('phone')
        message= request.form.get('message')

        entry = Contacts(name=name , phone_num = phone , msg = message , date= d.today(), email = email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from learn2_cod' + name , 
                    sender = email ,
                    recipients = [params['gmail-user']] ,
                    body = message +  "\n"  + phone
                    )

    return render_template('contact1.html' , params = params)

@app.route("/signup")
def signup():
    return render_template('signup.html',params=params)

@app.route("/signup" , methods = ['POST'])
def signup_post():
        # '''Add entry to DB'''
    name = request.form.get('name')
    username  = request.form.get('uname')
    email= request.form.get('email')
    password = request.form.get('pass')
    confirmpassword  = request.form.get('cpass')

    email_exist = Registration.query.filter_by(email=email).first()
    username_exist = Registration.query.filter_by(username=username).first()
    

    if email_exist:
        flash(email_exist)
        flash(" Email already exists!")
    
    elif username_exist:
        flash("Username Already Taken !")
        flash('Try Different Username!')
    elif password!= confirmpassword:
        flash("Password not same! ")
        flash("Try Again!")
    else:
        entry = Registration(name=name , username = username, pasword=generate_password_hash(password, method='sha256'), email = email)
        db.session.add(entry)
        db.session.commit()
        flash("You are Succefully Registered!")
        return redirect('/login') 
    return redirect('/signup')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect("/")

@app.route('/login')
def login():
    return render_template('login.html',params=params)

@app.route("/login" , methods = ['POST'])
def login_post():
    '''Add entry to DB'''
    session['username'] = request.form['uname'] 
    session['password'] = request.form['pass']
    remember = True if request.form.get('remember') else False
    user = Registration.query.filter_by(username=session['username'] ).first()
    session['name'] = Registration.query.filter_by(username =session['username']).first().name
    session['email'] = Registration.query.filter_by(username =session['username']).first().email
    
    if not user and not check_password_hash(user.password, session['password']):
        flash('Please check your login details and try again.')
        return redirect('/login')

    
    session['logged_in'] = True
    return redirect('/')
    
    # return render_template('login.html' , params = params)
@app.route("/profile")
def profile():
    return render_template('profile.html',params=params)

@app.route("/profile" , methods = ['POST'])
def profile_post():
        # '''Add entry to DB'''
    if request.method=='POST':
        # nam = request.form.get('name')
        email= request.form.get('email')
        img = request.form.get('img')

    
        email_exist = Registration.query.filter_by(email=email).first() 

        if email_exist:
            flash(email_exist)
            flash(" Email already exists!")

        else:
            user = Registration.query.filter_by(username = session['username']).first()
            user.email = email; session['email']= email
            db.session.commit()
            flash("Succefully Updated!")
            return redirect('/') 
        return redirect('/profile')



login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Registration.get(user_id)
if __name__ == '__main__':
    # flaskapp.run(debug=True)
    app.run(debug=True)



#auth_username=anujarya6121998@gmail.com
#auth_password=arya@#1998