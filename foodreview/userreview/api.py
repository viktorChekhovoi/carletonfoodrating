from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

SAYLES = "sayles-hill-cafe"
BURTON = "burton"
LDC = "east-hall"
ANDERSON = "schulze-cafe"
WEITZ = "weitz-cafe"

requestPrefix = "https://carleton.cafebonappetit.com/cafe/"
diningHalls = ["schulze-cafe", "sayles-hill-cafe", "weitz-cafe", "east-hall", "burton"]

def getCafeLink(cafe: str) -> str:
    assert cafe in diningHalls

    
    return f"{requestPrefix}{cafe}"



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

