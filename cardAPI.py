from flask import Flask, jsonify, request
from webscraper import getAllCards
import random
import treeKD

app = Flask(__name__)


# TODO: Remove this build and create the tree through put methods instead
card_dict = getAllCards()
# Store cards by attributes using a K-D tree for faster searching
tree = treeKD.TreeKD(card_dict)

# TODO: Return the first 10 results for a search lexicographically if there are too many results and allow for a page number in the request

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

# Search cards by attribute (Deprecated and incorrect)
# @app.route('/cards/attribute/<string:attribute>', methods=['GET'])
# def get_cards_by_attribute(attribute):
#     attribute = attribute.lower()
#     cards = [card for card in card_dict.values() if card.get('Attribute', '').lower() == attribute]
#     return jsonify(cards)

# Search for A SINGLE card by multiple attributes
@app.route('/cards/search/<string:attributes>', methods=['GET'])
def search_cards(attributes):
    attributes = attributes.lower().split(',')
    results = []
    for card in card_dict.values():
        if all(card.get(attr.strip(), '').lower() == attr.strip() for attr in attributes):
            results.append(card)
    return jsonify(results)

# TODO: Search for multiple cards by multiple attributes

# Return a random card from the database
@app.route('/cards/random', methods=['GET'])
def get_random_card():
    card = random.choice(list(card_dict.values()))
    return jsonify(card)

# TODO: Create an autocomplete function using the trie I will create for search by name

if __name__ == '__main__':
   app.run(port=5000)
