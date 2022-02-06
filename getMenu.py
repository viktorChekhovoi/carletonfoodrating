from bs4 import BeautifulSoup
import requests, json
from xml.etree.ElementTree import fromstring
from xmljson import parker, Parker
from lxml import etree


class Parser():

    def __init__(self, diningHall: str):
        self.diningHall = diningHall
        if (self.diningHall == "ldc"):
            self.webPage = "https://carleton.cafebonappetit.com/cafe/east-hall/"
        else:
            self.webpage = "https://carleton.cafebonappetit.com/cafe/burton/"
        self.menuLink = ""

    def isOpen(self):
        xpath = '//*[@id="cafe-hours"]/div/div/div/div[2]/div[1]/div'
        result = requests.get(self.webpage)
        soup = BeautifulSoup(result.content, "html.parser")
        dom = etree.HTML(str(soup))
        status = dom.xpath(xpath)[0].text
        print(status)
        return status != "Currently Closed"


    def getMenu(self):
        menuXpath = ""
        if self.isOpen():
            print("open")
            menuXpath = '//*[@id="site-panel__daypart-print-menu-61ff0d5092af0"]/li[2]/a'
        else:
            print("closed")
            menuXpath = '//*[@id="site-panel__daypart-print-menu-61ff45ccbc29c"]/li[2]/a'
        result = requests.get(self.webpage)
        soup = BeautifulSoup(result.content, "html.parser")
        dom = etree.HTML(str(soup))
        menu = dom.xpath(menuXpath)
        print(menu)
        self.menu = requests.get(menu[0].attrib['href'])
        return self.menu
