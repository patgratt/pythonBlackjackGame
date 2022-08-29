# we need random to shuffle the deck prior to dealing
import random

""" we'll use tuples to store the suits and ranks, this makes sense as they are ordered,
    immutable, and the items inside cannot be changed or erased """
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

# use hashmap (dictionary) to assign numerical values to the ranks
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
             "Queen":10, "King":10, "Ace":11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    """ give the card class a string method where, when asked to print a card, it will return
        the  suit and rank of the card """
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck  =  [] # start with an empty list
        """ usually nested for loops are no bueno but there's only ever 52 cards in a deck so doesn't really mattter here"""
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # build Card objects and add them to the list
    
    # utilize the shuffle method from the random module and apply it to our deck class
    def shuffle(self):
        random.shuffle(self.deck)

    # deal method pops a card from the top of the deck and returns it
    def deal(self):
        single_card = self.deck.pop()
        return single_card

    """ method to print out the contents of the entire deck, this isn't entirely necessary but will likely help with troubleshooting"""
    def __str__(self):
        deck_contents = ''  # start with empty string
        for card in self.deck:
            deck_contents += '\n ' + card.__str__() # add each Card object's print string
        return "The deck has: " + deck_contents


class Hand:
    def __init__(self):
        self.cards = [] # initiate cards attribute
        self.value = 0 # initiate value attribute
        self.aces = 0 # here we'll give aces their own attribute as they have the special behavior of taking on multiple values

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]





# testing
def test():
    test_deck = Deck()
    test_deck.shuffle()
    test_player = Hand()
    test_player.add_card(test_deck.deal())
    test_player.add_card(test_deck.deal())
    print(test_player.value)

test()