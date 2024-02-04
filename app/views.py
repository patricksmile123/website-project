from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime
import random
from temp_app import LoginForm, SignupForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/datetime')
def date_time():
    now = datetime.now()
    return render_template('datetime.html', now=now)


@app.route('/divisors/<int:n>')
def divisors(n):
    divisor = []
    for number in range(1, n + 1):
        if n % number == 0:
            divisor.append(number)
    return render_template('divisors.html', divisor=divisor)


@app.route('/quotes')
def quotes():
    quotes_text = open("app/data/quotes.txt", 'r').readlines()
    random_number = random.randint(1, 99)
    quote = str(quotes_text[random_number])
    return render_template('quotes.html', quote=quote)


@app.route('/abbreviations')
def abbreviations():
    abbreviations_file = open("app/data/abbreviations.txt", 'r')
    x = abbreviations_file.read()
    y = x.split("\n")
    hash = "#"
    cleaned_file = []
    for line in y:
        if hash not in line:
            cleaned_file.append(line)
    for i in range(len(cleaned_file)):
        cleaned_file[i] = cleaned_file[i].replace("\t", "    ").strip()
    first10 = cleaned_file[:10]
    return first10


@app.route('/abbrev_dict')
def abbrev_dict():
    abbreviations_file = open("app/data/abbreviations.txt", 'r')
    x = abbreviations_file.read()
    y = x.split("\n")
    hash = "#"
    abbrev_dict = {}
    cleaned_file = []
    for line in y:
        if hash not in line:
            cleaned_file.append(line)
    for i in range(len(cleaned_file)):
        cleaned_file[i] = cleaned_file[i].replace("\t", "    ")
    for line in cleaned_file:
        key, value = line.strip().split("    ")[0:2]
        abbrev_dict[key] = value
    return abbrev_dict


@app.route('/abbrevsearch', methods=['GET', 'POST'])
def abbrevsearch():
    search_results = {}
    search_term = ""
    abbreviations = abbrev_dict()
    if request.method == 'POST':
        search_term = request.form['search_term']
    for abbreviation, full_form in abbreviations.items():
        if search_term in abbreviation.lower():
            search_results[abbreviation] = full_form
    return render_template('abbrevsearch.html', search_results=search_results)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign Up', form=form)