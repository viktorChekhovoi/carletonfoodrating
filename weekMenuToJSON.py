import requests
import json
from bs4 import BeautifulSoup
  
URL = "https://legacy.cafebonappetit.com/weekly-menu/370572"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib')

foodTypeRows = soup.find_all(class_="row")

menuOfWeek = {}

for i in range(0, 7):
	menuOfWeek[i] = {}

for foodTypeRow in foodTypeRows:
	foodTypeName = foodTypeRow.find(class_="spacer").string
	foodTypeRowColumns = foodTypeRow.find_all(class_="cell_menu_item")
	for day in range(0, 7):
		foodTypeRowColumnElements = [] 
		for foodTypeRowColumnElement in foodTypeRowColumns[day].find_all(class_="weelydesc"):
			foodTypeRowColumnElements.append(foodTypeRowColumnElement.text)
		menuOfWeek[day][foodTypeName] = foodTypeRowColumnElements

with open("menu_of_week.json", "w") as outfile:
    json.dump(menuOfWeek, outfile)