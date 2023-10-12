from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password1")

        user = User.query.filter_by(email=email).first()

        if user:
            curr_password = generate_password_hash(password, method="sha256")
            if curr_password == user.password:
                flash("Logged in", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect info", category="error")
        else:
            flash("User does not exist", category="error")
    
    return render_template("login.html", user=current_user)

@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #a few basic python checks
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Passwords must be at least 7 categories", category="error")
        else:
            new_user = User(email=email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
