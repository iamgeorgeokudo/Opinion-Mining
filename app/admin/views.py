from flask import render_template
from flask_login import login_required
from . import admin
from .. import db
from ..models import User, Role


@admin.route('/')
@login_required
def index():
    return render_template('admin/dashboard.html')


@admin.route('/users')
@login_required
def users():
    users_data = db.session.query(User.email, User.username) \
        .join(Role, User.role_id == Role.id).filter(Role.name == 'User').all()

    # get list users from the database

    return render_template('admin/users.html', users_data=users_data)


@admin.route('/insights')
@login_required
def insights():
    return render_template('admin/insights.html')
