from flask import render_template, redirect, url_for, flash
from . import main
from .forms import LoginForm, RegistrationForm, AnalysisForm


@main.route('/')
def index():
    return render_template('user/index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('user/login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('main.login'))
    return render_template('user/register.html', form=form)


@main.route('/about')
def about():
    return render_template('user/about.html')


@main.route('/contact')
def contact():
    return render_template('user/contact.html')


@main.route('/analyze', methods=['GET', 'POST'])
def analyze():
    form = AnalysisForm()
    if form.validate_on_submit():
        opinion_text = form.content.data
    return render_template('user/analyze.html', form=form)
