from flask import Flask, render_template ,request , session , redirect ,flash , url_for 
from functools import wraps
from flask_login import  UserMixin, login_required
import os , math
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists    

from socket import socket
from werkzeug.utils import secure_filename
from flask_mail import Mail
#from flask_mail import mail
import json
from datetime import datetime
from datetime import date as d
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

with open(r'C:\Users\DELL\AppData\Local\Programs\Python\Python37\Project flask\config.json', 'r') as c:
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

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

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
            return redirect(url_for('login'))

    return wrap
		

@app.route("/")
def home():
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
@login_required
def p():
    
    return render_template('practice.html' , params = params)

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




@app.route("/profile/<string:username>/" , methods = ['GET' , 'POST'])
@login_required
def profile(username):
    print(username)
    
    if request.method == 'POST':
        nam = request.form.get('name')
        
        email = request.form.get('email')
        password = request.form.get('pass')
        
        
        if session['user']==username:  
        
            user = Registration.query.filter_by(username = username).first()
            user.name  = nam
    
            user.email = email
            user.pasword = password
            
            db.session.commit()
            return redirect('/profile/' + username)
    
        user = Registration.query.filter_by(username = username).first()
        return render_template('profile.html' , params = params ,  username=username , user = user)
    else:
        
        return login()



@app.route("/uploader" , methods = ['GET' , 'POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_user']):

        if(request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] , secure_filename(f.filename)))
            return "Uploaded Successfully!"

@app.route("/logout")

def logout():
    global a
    a=0
    params['v']="login"
    session.pop('user')
   
    return redirect("/")
    

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


@app.route("/signup" , methods = ['GET' , 'POST'])
def Register():

    if ('username' in session and session['username']==Registration.query.filter_by(username).first()):
        flash('Already Login!')
    if request.method=='POST':

        '''Add entry to DB'''
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
            entry = Registration(name=name , username = username, pasword = password, email = email)
            db.session.add(entry)
            db.session.commit()
            flash("You are Succefully Registered!")
           
            return redirect ('/' )
    
    return render_template('signup.html' , params = params)



@app.route("/login" , methods = ['GET' ,'POST'])
def login():
    
    
    if request.method=='POST':
        '''Add entry to DB'''
      
        username = request.form['uname']
        password = request.form['pass']
        
       
        username = db.session.query(db.exists().where(Registration.username == username)).scalar()
        password = db.session.query(db.exists().where(Registration.pasword == password)).scalar()


        if username and password :
    
            global a
            a=1
            session['logged_in'] = True
            session['user']=username 
           
            return redirect("/")

        elif not username  or not password:
            flash("Try Again!")
            return redirect(url_for("login"))
    
    return render_template('login.html' , params = params)

app.run(debug=True)



#auth_username=anujarya6121998@gmail.com
#auth_password=arya@#1998