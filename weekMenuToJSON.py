import requests
import json
from bs4 import BeautifulSoup


def menu(URL: str):
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, "html5lib")

    foodTypeRows = soup.find_all(class_="row")

    menuOfWeek = {}

    for i in range(0, 7):
        menuOfWeek[i] = {}
        if i < 6:
            menuOfWeek[i]["Breakfast"] = {}
            menuOfWeek[i]["Lunch"] = {}
        else:
            menuOfWeek[i]["Brunch"] = {}
        menuOfWeek[i]["Dinner"] = {}

    for foodTypeRow in foodTypeRows:
        foodTypeName = foodTypeRow.find(class_="spacer").string
        foodTypeRowColumns = foodTypeRow.find_all(class_="cell_menu_item")

        for day in range(0, 7):
            breakfast = []
            lunch = []
            dinner = []
            brunch = []

            for foodTypeRowColumnElement in foodTypeRowColumns[day].find_all(
                class_="menu-item-description"
            ):
                mealName = foodTypeRowColumnElement.find(class_="weelydesc").text
                mealType = foodTypeRowColumnElement.find(class_="daypart-abbr").text
                if day < 6:
                    if mealType.find("[B") != -1:
                        breakfast.append(mealName)
                    if mealType.find("L") != -1:
                        lunch.append(mealName)
                else:
                    if mealType.find("Br") != -1:
                        brunch.append(mealName)
                if mealType.find("D") != -1:
                    dinner.append(mealName)

            if day < 6:
                menuOfWeek[day]["Breakfast"][foodTypeName] = breakfast
                menuOfWeek[day]["Lunch"][foodTypeName] = lunch
            else:
                menuOfWeek[day]["Brunch"][foodTypeName] = brunch

            menuOfWeek[day]["Dinner"][foodTypeName] = dinner
