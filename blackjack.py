# we need random to shuffle the deck prior to dealing
import random

""" we'll use tuples to store the suits and ranks, this makes sense as they are ordered,
    immutable, and the items inside cannot be changed or erased """
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

# use hashmap (dictionary) to assign numerical values to the ranks
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
             "Queen":10, "King":10, "Ace":11}



