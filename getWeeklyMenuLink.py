from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

diningHallsNumberToStrings = {
    0: "schulze-cafe",
    1: "sayles-hill-cafe",
    2: "weitz-cafe",
    3: "east-hall",
    4: "burton"
}

diningHalls = []
diningHalls.append(Request("https://carleton.cafebonappetit.com/cafe/schulze-cafe/"))
diningHalls.append(Request("https://carleton.cafebonappetit.com/cafe/sayles-hill-cafe/"))
diningHalls.append(Request("https://carleton.cafebonappetit.com/cafe/weitz-cafe/"))
diningHalls.append(Request("https://carleton.cafebonappetit.com/cafe/east-hall/"))
diningHalls.append(Request('https://carleton.cafebonappetit.com/cafe/burton/'))

with open("links.txt", "w") as output:
    for i in range(0, 5):
        html_page = urlopen(diningHalls[i])
        soup = BeautifulSoup(html_page, "html5lib")

        for link in soup.findAll('a'):
            if link.get('href'):
                if link.get('href').find("https://legacy.cafebonappetit.com/weekly-menu/") != -1:
                    output.write(diningHallsNumberToStrings[i] + ": ")
                    output.write(link.get('href') + '\n')
                    break

# links = []

# for link in soup.findAll('a'):
#     links.append(link.get('href'))

