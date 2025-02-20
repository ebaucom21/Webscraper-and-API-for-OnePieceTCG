from bs4 import BeautifulSoup
import requests

# Card dictionary to store info for the cards
# Key - ID of the card
# Value - A dictionary that holds all the info about the cards
# Value Dictionary Key - The attribute (eg. Power, Cost, Name)
# Value Dictionary Value - The respective attributes value
cardDict = {}

# Url to the one piece official card list site
# This source code can also be referenced using ctrl + shift + i
url = "https://en.onepiece-cardgame.com/cardlist/"
# Use a request to grab the html from the site
response = requests.get(url, timeout=5)
# Parse the html into a Beautiful Soup object
content = BeautifulSoup(response.content,"html.parser")

# TODO: Create a way to parse through every single set in the site.

# Go through each individual card in the set
for card in content.find_all('dl', attrs = {"class":"modalCol"}):
    # Cards will be duplicated in this url source if they have different arts
    # To check if this is a different art you must check the ID as some cards will have the same name but different ID
    # Example - OP09-001 and OP09-001_p1 are the same Shanks but OP09-001 and OP01-120 are not the same Shanks
    id = str(card.attrs['id'])[0:8]
    name = card.find('div', attrs={"class":"cardName"}).text
    if id in cardDict:
        # Only update the image
        continue
    else:
        continue
    
    

    