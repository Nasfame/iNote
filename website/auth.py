from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash as genr, check_password_hash as checkr
from .import db
from models import User
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint("auth",__name__)


@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        __pass__ = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if checkr(user.password,__pass__):
                login_user(user,remember=True)
                flash('Logged In ',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password ',category='error')
        else:
            flash('Invalid User', category='error')

    return render_template("login.html",user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods = ['GET','POST'])
def sign_up():
    if request.method =='POST':
        data = request.form
        email = data.get('email')
        first_name = data.get('firstName')
        pass1 = data.get('password1')
        pass2 = data.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
          flash('Email already Exists',category ='error')
        elif len(email)<6:
            flash('Email must be greater than 6 characters ',category='error')
        elif len(first_name)<2:
            flash('firstName must be greater than 2 characters ',category='error')
        elif pass1 !=pass2:
            flash('Passwords don\'t match ', category='error')
        else:
            new_user = User(email = email,firstName = first_name,password = genr(pass1,method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created',category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html",user = current_user)