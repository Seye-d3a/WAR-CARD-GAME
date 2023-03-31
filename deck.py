class Deck():
    
    def __init__(self):
        #in a deck there's 52 cards so we want all cards
        #we're not taking user input cause all card decks should be the same without input from the user
    
        self.all_cards = []
        
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