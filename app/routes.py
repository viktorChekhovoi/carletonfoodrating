from urllib import request
from flask import render_template
from app import app, db
from app.forms import RateForm
from app.models import DiningHall, Station, Food, Rating
from flask import render_template, flash, redirect
from app.getMenu import Parser



def getBurtonJson():
    parser = Parser("burton")
    burtonMenu = {}
    burton = {"Burton": {"status": parser.isOpen(), "menu": burtonMenu}}


def makeForms(menus: str):
    forms = dict()
    for station in menus:
        #print(station)
        for foodItem in menus[station]:
            if station not in forms:
                forms[station] = {}
            newForm = RateForm()
            newForm.name = f'{station}:{foodItem}'
            forms[station][foodItem["name"]] = newForm
    return forms


def updateAverage(food):
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
        return averageRating
    return food.averageRating



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    food = {"Pizza": [{"name": "Cheese", "rate": 9}, {"name": "Pepperoni", "rate": 8}]}
    
    forms = makeForms(food)
    parser = Parser("burton")
    print(parser.isOpen())
    parser.getMenuHtml()
    for station in forms:
        for food in forms[station]:
            if forms[station][food].validate_on_submit():
                food.averate_rating = updateAverage(food)
                return redirect('/index')
                
    food = {"Pizza": [{"name": "Cheese", "rate": 9}, {"name": "Pepperoni", "rate": 8}]}
    return render_template('index.html', food=food, forms=forms)
