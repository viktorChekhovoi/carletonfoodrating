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


    def setMenu(self):
        kettles_xpath = ""
        if self.isOpen():
            print("open")
            kettles_xpath = '//*[@id="site-panel__daypart-print-menu-61ff0d5092af0"]/li[2]/a'
        else:
            print("closed")
            kettles_xpath = '//*[@id="site-panel__daypart-print-menu-61ff0c2d3a111"]/li[2]/a'
        result = requests.get(self.webpage)
        soup = BeautifulSoup(result.content, "html.parser")
        dom = etree.HTML(str(soup))
        kettles = dom.xpath(kettles_xpath)
        self.menu = requests.get(kettles[0].attrib['href'])


    def getDailyMenu(self, day: str):
        soup = BeautifulSoup(self.menu.content, "html.parser")
        dom = etree.HTML(str(soup))
        assert(self.menuLink != "")

        monday = {}
        tuesday = {}
        wednesday = {}
        thursday = {}
        friday = {}
        saturday = {}
        sunday = {}

        kettlesXpath = '/html/body/div[1]/div[2]/div[2]'
        kettles = dom.xpath(kettlesXpath)
        for child in kettles:
            if child.attrib['class'] != 'spacer day':
                item = child[0][0][0][0]
                print(item.text)

        '//*[@id="menu-item-18620566"]/div[1]/strong/span'
        breakfastGrillXpath = '/html/body/div[1]/div[2]/div[3]'
        bGrill = dom.xpath(breakfastGrillXpath)
        breakfastSkilletXpath = '/html/body/div[1]/div[2]/div[4]'
        bSkillet = dom.xpath(breakfastSkilletXpath)
        breakfastXpath = '/html/body/div[1]/div[2]/div[5]'
        breakfast = dom.xpath(breakfastXpath)
        nourishXpath = '/html/body/div[1]/div[2]/div[6]'
        nourish = dom.xpath(nourishXpath)
        grillXpath = '/html/body/div[1]/div[2]/div[7]'
        grill = dom.xpath(grillXpath)
        pizzaXpath = '/html/body/div[1]/div[2]/div[8]'
        pizza = dom.xpath(pizzaXpath)
        pastaXpath = '/html/body/div[1]/div[2]/div[9]'
        pasta = dom.xpath(pastaXpath)
        globalXpath = '/html/body/div[1]/div[2]/div[10]'
        globalMenu = dom.xpath(globalXpath)
        dessertXpath = '/html/body/div[1]/div[2]/div[11]'
        dessert = dom.xpath(dessertXpath)

        #match day:
            #case "monday":
                

                 



#burtonJson = json.dumps(parker.data(fromstring(str(burtonWebpage.text))))




# What we need to extract:
# Is it open or closed
# Each category
# Within each category, every menu item in it