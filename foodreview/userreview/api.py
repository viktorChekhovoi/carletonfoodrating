from typing import TypedDict
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import re
from menu import Menu
import requests
from constants import *


def getCafeLink(cafe: str) -> str:
    return f"{REQUEST_PREFIX}{cafe}"


def getCurrentWeekMenuLink(cafe: str) -> str:
    assert cafe in DINING_HALLS, f"invalid cafeteria: {cafe}"
    cafeLink: str = getCafeLink(cafe)
    bonAppetitCompleteWebpage: str = requests.get(cafeLink).content.__str__()
    getLinkPattern: str = r"https://legacy\.cafebonappetit\.com/weekly-menu/[^\']*"
    currentWeekMenuLink: str = re.findall(
        pattern=getLinkPattern, string=bonAppetitCompleteWebpage
    )[0]

    return currentWeekMenuLink


def getWeeklyStationMenu(cafe: str) -> Menu:
    """
    Returns a dictionary weekMenu, where weekMenu[day of the week][station]
    is the list of food available at a given station at a given time of day
    """
    currentWeekMenuLink = getCurrentWeekMenuLink(cafe)
    thisWeeksMenu = requests.get(currentWeekMenuLink).content

    bs4Search = bs(thisWeeksMenu, "html.parser")
    for station in bs4Search.find_all("div", {"class": ["row", "row odd"]}):
        stationName = station.find("span", {"class": ["stationname"]}).text
        print(stationName)


getWeeklyStationMenu(BURTON)
