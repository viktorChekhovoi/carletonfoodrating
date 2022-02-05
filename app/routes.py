from urllib import request
from flask import render_template
from app import app
from app.forms import RateForm
from flask import render_template, flash, redirect


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    food = {"Pizza": [{"name": "Cheese", "rate": 9}, {"name": "Pepperoni", "rate": 8}]}
    form = RateForm()
    if form.validate_on_submit():
        flash(f'Rated an item {form.rating.data} out of 10')
        return redirect('/index')
    return render_template('index.html', food=food, form=form)
