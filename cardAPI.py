import json
from flask import Flask, jsonify, request
from webscraper import getAllCards
import random

app = Flask(__name__)
card_dict = getAllCards()
# TODO: Store cards by attributes using a trie or other data structure for faster search
# TODO: Only return the first 10 results for a search  lexicographically if there are too many results and allow for a page number in the request

# Get all cards in the database
@app.route('/cards', methods=['GET'])
def get_cards():
    return jsonify(card_dict)

# Get a specific card by ID
@app.route('/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = card_dict.get(card_id)
    if card:
        return jsonify(card)
    else:
        return jsonify({"error": "Card not found"}), 404

# Search cards by attribute
@app.route('/cards/attribute/<string:attribute>', methods=['GET'])
def get_cards_by_attribute(attribute):
    attribute = attribute.lower()
    cards = [card for card in card_dict.values() if card.get('Attribute', '').lower() == attribute]
    return jsonify(cards)

# Search for a card by multiple attributes
@app.route('/cards/search/<string:attributes>', methods=['GET'])
def search_cards(attributes):
    attributes = attributes.lower().split(',')
    results = []
    for card in card_dict.values():
        if all(card.get(attr.strip(), '').lower() == attr.strip() for attr in attributes):
            results.append(card)
    return jsonify(results)

# Return a random card from the database
@app.route('/cards/random', methods=['GET'])
def get_random_card():
    card = random.choice(list(card_dict.values()))
    return jsonify(card)

# TODO: Create an autocomplete function using the trie I will create by name

if __name__ == '__main__':
   app.run(port=5000)
