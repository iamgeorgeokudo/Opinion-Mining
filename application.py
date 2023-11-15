import os

from flask import render_template
from flask.cli import AppGroup
from flask_migrate import Migrate

from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('OPINIONMINING_CONFIG') or 'default')
migrate = Migrate(app, db)
admin_cli = AppGroup('admin')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


@admin_cli.command('create')
def create_admin():
    from werkzeug.security import generate_password_hash
    admin_role = Role.query.filter_by(name='Admin').first()
    if not admin_role:
        admin_role = Role(name='Admin')
        db.session.add(admin_role)
        db.session.commit()
    username = input('Enter username: ')
    email = input('Enter email: ')
    password = input('Enter password: ')

    # create admin user
    admin_user = User(username=username, email=email, password=generate_password_hash(password), role=admin_role)
    db.session.add(admin_user)
    db.session.commit()
    print('Admin created successfully')


app.cli.add_command(admin_cli)
