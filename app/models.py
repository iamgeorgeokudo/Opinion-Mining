from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(60), unique=True, index=True)
    password_hash = db.Column(db.String(60))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    messages = db.relationship('Message', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    Users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.Text)


# user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
