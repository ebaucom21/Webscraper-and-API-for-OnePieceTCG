import pytest
from newWebscraper import webScraper 

# TODO: Patch these as they are all currently filler templates

def test_AllCards():
    # Test the AllCards function
    webscraper = webScraper("https://en.onepiece-cardgame.com/cardlist/") # Update with the correct URL if needed
    cards = webscraper.getAllCards()
    assert isinstance(cards, list), "AllCards should return a list of cards."
    assert len(cards) > 0, "AllCards should return a non-empty list."
    
def test_CardBySet():
    # Test the CardBySet function with a known set
    webscraper = webScraper("https://en.onepiece-cardgame.com/cardlist/") # Update with the correct URL if needed
    set_name = "OP01"  # Example set name
    cards = webscraper.getCardBySet(set_name)
    assert isinstance(cards, list), f"CardBySet should return a list of cards for set {set_name}."
    assert len(cards) > 0, f"CardBySet should return a non-empty list for set {set_name}."
    
def test_CardByID():
    # Test the CardByID function with a known card ID
    webscraper = webScraper("https://en.onepiece-cardgame.com/cardlist/") # Update with the correct URL if needed
    card_id = "OP01-001"  # Example card ID
    card = webscraper.getCardByID(card_id)
    assert isinstance(card, dict), f"CardByID should return a dictionary for card ID {card_id}."
    assert "Name" in card, f"CardByID should return a card with a 'Name' key for card ID {card_id}."
    assert card["Name"] == "Monkey D. Luffy", f"CardByID should return the correct name for card ID {card_id}."