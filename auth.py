from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('main.make_picks', username=user.name))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
