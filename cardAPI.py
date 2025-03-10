import json
from flask import Flask, jsonify, request
from webscraper import getAllCards

app = Flask(__name__)
card_dict = getAllCards()
# TODO: Store cards by attributes using a trie

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


if __name__ == '__main__':
   app.run(port=5000)
