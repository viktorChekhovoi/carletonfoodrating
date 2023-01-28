from email.policy import default
from urllib import request
from flask import render_template, request
from app import app, db, foods
from app.forms import RateForm
from app.models import DiningHall, Station, Food, Rating
from flask import render_template, flash, redirect
from getMenu import Parser
from getWeekMenu import MenuParser
from collections import defaultdict


def getBurtonJson():
    parser = Parser("burton")
    burtonMenu = {}
    burton = {"Burton": {"status": parser.isOpen(), "menu": burtonMenu}}


def makeForms(menus: str):
    forms = dict()
    for meal in menus:
        if meal not in forms:
            forms[meal] = dict()
        for station in menus[meal]:
            if len(menus[meal][station]) != 0:
                if station not in forms[meal]:
                    forms[meal][station] = {}
                for foodItem in menus[meal][station]:
                    newForm = RateForm()
                    newForm.name = f"{meal}:{station}:{foodItem}"
                    forms[meal][station][foodItem] = {}
                    forms[meal][station][foodItem]["form"] = newForm
                    food_db = Food.query.filter_by(name=foodItem).all()[0]
                    try:
                        forms[meal][station][foodItem]["rate"] = "{:.2f}".format(
                            food_db.rating()
                        )
                    except:
                        forms[meal][station][foodItem]["rate"] = 0.0
    return forms


def updateAverage(food, form):
    newRating = Rating(rating=form.rating.data, foodRated=food)
    db.session.add(newRating)
    db.session.commit()
    total = 0
    numRatings = 0
    allRatings = Rating.query.filter_by(foodRated=food).all()
    for rating in allRatings:
        numRatings += 1
        total += rating.rating

    averageRating = total / numRatings
    return averageRating


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    forms = makeForms(foods)
    for meal in forms:
        for station in forms[meal]:
            for foodItem in forms[meal][station]:
                form = forms[meal][station][foodItem]["form"]
                if form.validate_on_submit():
                    if request.form["fieldName"] == f"{foodItem}:{station}":
                        food_db = Food.query.filter_by(name=foodItem).all()
                        if len(food_db) == 0:
                            return redirect("/")
                        food_db = food_db[0]
                        food_db.averate_rating = updateAverage(food_db, form)
                        db.session.add(food_db)
                        db.session.commit()
                        return redirect("/")

    return render_template("index.html", food=foods, forms=forms)
