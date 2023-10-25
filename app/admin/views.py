from flask import render_template, redirect, url_for, flash
from . import admin
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm


@admin.route('/')
def index():
    return render_template('admin/dashboard.html')


@admin.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/users')
def users():
    return render_template('admin/users.html')


@admin.route('/feedback')
def feedback():
    return render_template('admin/feedback.html')


@admin.route('/insights')
def insights():
    return render_template('admin/insights.html')
