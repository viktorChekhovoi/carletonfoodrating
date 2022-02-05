from urllib import request
from flask import render_template
from app import app, db
from app.forms import RateForm
from app.models import DiningHall, Station, Food, Rating
from flask import render_template, flash, redirect


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    food = {"Pizza": [{"name": "Cheese", "rate": 9}, {"name": "Pepperoni", "rate": 8}]}
    forms = dict()
    for station in food:
        #print(station)
        for foodItem in food[station]:
            if station not in forms:
                forms[station] = {}
            newForm = RateForm()
            newForm.name = f'{station}:{foodItem}'
            forms[station][foodItem["name"]] = newForm

    print(forms)

    for station in forms:
        for food in forms[station]:
            if forms[station][food].validate_on_submit():
                #station_db = Station.query.filter_by(name=station).all()[0]
                food_db = Food.query.filter_by(name=food).all()
                if len(food_db) != 0:
                    food_db = food_db[0]
                    newRating = Rating(rating=food.rating.data, foodRated=food_db)
                    db.session.add(newRating)
                    total = 0
                    numRatings = 0
                    allRatings = Rating.query.filter_by(foodRated=food_db).all()
                    for rating in allRatings:
                        numRatings += 1
                        total += rating.rating

                    averageRating = total/numRatings

                    food.averate_rating = averageRating

                return redirect('/index')
                
    food = {"Pizza": [{"name": "Cheese", "rate": 9}, {"name": "Pepperoni", "rate": 8}]}
    return render_template('index.html', food=food, forms=forms)
