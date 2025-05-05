from bs4 import BeautifulSoup
import requests

class webScraper:
    # Constructor will take in the url to the official one piece card game site
    def __init__(self,url="https://en.onepiece-cardgame.com/cardlist/"):
        # The url of the site to scrape
        self.url = url
        
    # This function will return an array of all the cards in one piece TCG
    def getAllCards(self):
        # TODO: Go through every set and call getSet for each set
        allCards = []
        # Use a request to grab the html from the site
        response = requests.get(self.url, timeout=5)
        # Parse the html into a Beautiful Soup object
        content = BeautifulSoup(response.content,"html.parser")
        # Find every available set in the site
        sets = []
        # This complicated line simply just goes to the place in html where the sets are located
        for setName in content.find("body", attrs={"id":"cardlist"}).find("main",attrs={"class":"mainCol"}).find("article").find("div", attrs={"class":"contentsWrap isIndex"}).find("div", attrs={"class":"searchCol"}).find("form",attrs={"method":"post"}).find("div",attrs={"class":"formsetDefaultArea"}).find("div",attrs={"class":"seriesCol"}).find("select",attrs={"name":"series"}).find_all("option"):
            print(setName.text)
        
        
        
        return allCards
    
    # This function will return an array of all the cards in a set
    def getCardBySet(self, set):
        # TODO: Parse through a set and return all the cards in the set
        setCards = []
        
        
        return setCards
    
    # This function will return all cards of a specific ID
    def getCardByID(self, id):
        # TODO: Parse through every set and then return a card with the specific ID
        # Make sure to continue to the next set even if the card is found to grab every art
        card = None
        
        
        
        return card