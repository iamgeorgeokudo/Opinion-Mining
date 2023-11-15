from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from app import db
from . import main
from .forms import AnalysisForm, MessageForm
from ..models import Message, Role


@main.route('/')
@login_required
def index():
    return render_template('user/index.html')


@main.route('/about')
@login_required
def about():
    return render_template('user/about.html')


@main.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(message=form.message.data)
        db.session.add_all(message)
        db.session.commit()
        flash('Message entered successfully')
    return render_template('user/contact.html', form=form)


@main.route('/analyze', methods=['GET', 'POST'])
@login_required
def analyze():
    form = AnalysisForm()
    if form.validate_on_submit():
        opinion_text = form.content.data
    return render_template('user/analyze.html', form=form)



