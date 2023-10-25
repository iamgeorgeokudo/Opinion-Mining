from flask import render_template
from . import admin
from werkzeug.security import generate_password_hash, check_password_hash


@admin.route('/')
def index():
    return render_template('admin/dashboard.html')


