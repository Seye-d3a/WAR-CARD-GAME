class Player():
    
    def __init__(self,name):
        self.name= name
        
        self.allcards = []
        
    def remove_card(self):
        return self.allcards.pop(0)
    
    def add_cards(self,new_card):
        if type(new_card)== type([]): #if we're adding a list of cards(multiple cards)
            self.allcards.extend(new_card)
        else:
            self.allcards.append(new_card) #If we're adding only one card
    
    def __str__(self):
        if len(self.allcards)==1:
            return f"{self.name} has {len(self.allcards)} card."
        else:
            return f"{self.name} has {len(self.allcards)} cards."