from cards import Card
import random
class Deck():
    
    def __init__(self):
        #in a deck there's 52 cards so we want all cards
        #we're not taking user input cause all card decks should be the same without input from the user
    
        self.all_cards = []
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
        values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

        for suit in suits:
            for rank in ranks:
                card_deck= Card(suit,rank)
                
                self.all_cards.append(card_deck)
    
    #now to shuffle the cards
    #note: I already imported random at the global level
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    #Now to deal the cards
    
    def deal(self):
        delt_card = self.all_cards.pop()
        return delt_card