import app
from app import models
from app.models import *

burton = DiningHall.query.all()[0]
ldc = DiningHall.query.all()[1]

burton_kettle = Station(name="Kettle", hall=burton)
burton_nourish = Station(name="Nourish", hall=burton)
burton_grill = Station(name="Grill", hall=burton)
burton_pasta = Station(name="Pasta", hall=burton)
burton_global = Station(name="Global", hall=burton)

ldc_cereal = Station(name="Hot Cereal", hall=ldc)
ldc_soup = Station(name="Soup", hall=ldc)
ldc_cucina = Station(name="Cucina", hall=ldc)
ldc_american = Station(name="American Regional", hall=ldc)
ldc_pizza = Station(name="Cucina Pizza", hall=ldc)
ldc_deli = Station(name="Market Deli", hall=ldc)

db.session.add(burton_kettle)
db.session.add(burton_nourish)
db.session.add(burton_grill)
db.session.add(burton_pasta)
db.session.add(burton_global)

db.session.add(ldc_cereal)
db.session.add(ldc_american)
db.session.add(ldc_cucina)
db.session.add(ldc_deli)
db.session.add(ldc_pizza)
db.session.add(ldc_soup)


print("Added everything\n\n\n")
print(Station.query.where(Station.hall==burton).first())