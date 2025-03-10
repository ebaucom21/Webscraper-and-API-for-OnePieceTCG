from bs4 import BeautifulSoup
import requests

# This function will scrape the one piece card game website for all the cards and their info
# The info will be stored in a dictionary and returned to the caller
def getAllCards():
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
        if id in cardDict:
            # Only update the image and set if applicable
            imgSrc = card.find('img', attrs={"class":"lazy", "alt":name}).attrs['data-src']
            imgSrc = 'https://en.onepiece-cardgame.com' + imgSrc[2:len(imgSrc)]
            curList = cardDict[id]["Image"]
            curList.append(imgSrc)
            cardDict[id]["Image"] = curList
            
            # Prune the front text off
            sets = card.find('div',attrs={"class":"getInfo"}).text
            sets = sets[12:len(sets)]
            curSets = cardDict[id]["Sets"]
            if sets not in curSets:
                curSets.append(sets)
            cardDict[id]["Sets"] = curSets
            
            continue
        else:
            name = card.find('div', attrs={"class":"cardName"}).text
            
            # Need to add the link to the home page as the source code only contains the extensions
            imgSrc = card.find('img', attrs={"class":"lazy", "alt":name}).attrs['data-src']
            imgSrc = 'https://en.onepiece-cardgame.com' + imgSrc[2:len(imgSrc)]
            imgSrc = [imgSrc]
            
            # Need to prune it to only the number
            cost = card.find('div', attrs={'class':'cost'}).text
            cost = cost[4:len(cost)]
            
            # If they are not a character/leader they do not have an attribute which we will represent as "-"
            attribute = card.find('div', attrs={'class':'attribute'}).find('i').text
            if str(attribute) == "":
                attribute = "-"
            
            # Need to prune it to only the number
            # Already a dash for cards that do not have power
            power = card.find('div',attrs={"class":"power"}).text
            power = power[5:len(power)]
            
            # Need to prune it to only the number
            # Already a dash for cards that do not have a counter
            counter = card.find('div',attrs={"class":"counter"}).text
            counter = counter[7:len(counter)]
            
            # Need to prune it to only the color
            color = card.find('div',attrs={"class":"color"}).text
            color = color[5:len(color)]
            
            # Need to create a list from the text as cards can have more then one feature type
            featureText = card.find('div',attrs={"class":"feature"}).text
            featureText = featureText[4:len(featureText)]
            featureList = featureText.split("/")
            
            # Need to split up the text into their seperate lines in a list
            text = card.find('div',attrs={"class":"text"})
            text = str(text)
            text = text[33:len(text)-6]
            text = text.split("<br/>")
            
            # Prune the front text off
            sets = card.find('div',attrs={"class":"getInfo"}).text
            sets = sets[12:len(sets)]
            sets = [sets]
            
            # Store the info into the dictionary
            info = {"ID":id,"Name":name,"Image":imgSrc,"Cost":cost,"Attribute":attribute,"Power":power,"Counter":counter,"Color":color,"Types":featureList,"Text":text,"Sets":sets}
            cardDict[id] = info
            
            continue
        
    return cardDict
    