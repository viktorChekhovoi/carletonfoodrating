from calendar import weekday
from datetime import datetime
import app
from app import models
from app.models import *
from getWeekMenu import MenuParser

DiningHall.query.delete()
Station.query.delete()
Food.query.delete()
print("Deleted old data")

burton = DiningHall(name="Burton")
# ldc = DiningHall(name="LDC")
db.session.add(burton)
# db.session.add(ldc)
db.session.commit()
print("Added dining halls")

parser = MenuParser()
currentMenu = parser.parseToday()
burtonStations = currentMenu["Dinner"].keys()
stations = {}
for station in burtonStations:
    stations[station] = Station(name=station, hall=burton)
    db.session.add(stations[station])

db.session.commit()
print("Added stations\n\n\n")
for meal in currentMenu:
    for station in currentMenu[meal]:
        for foodItem in currentMenu[meal][station]:
            db.session.add(
                Food(
                    name=foodItem,
                    averate_rating=1.5,
                    station_location=stations[station],
                )
            )

db.session.commit()

print("Added foods")
