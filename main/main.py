from cards import Card
from deck import Deck
from player import Player


player1= Player('Player1')
player2= Player('PLayer2')

game_deck = Deck()
game_deck.shuffle()

#split the deck between both player instances

for x in range(26):
    
    player1.add_cards(game_deck.deal()) #26 cards delt from the game_deck will go to player1
    player2.add_cards(game_deck.deal()) #26 of cards delt from the game_deck will go to player2

#while game_on
game_on= True

round_num = 0 #This is our count
while game_on:
    
    round_num +=1
    print(f"Round {round_num}")
    
    #Checking for who has 0 cards first
    if len(player1.allcards)== 0:
        print("Player1 out of cards, PLayer2 wins the game!")
        game_on = False
        break
    elif len(player2.allcards) == 0:
        print("Player2 out of cards, Player1 wins the game!")
        game_on = False
        break
    #START A NEW ROUND
    player1_cards = []
    player1_cards.append(player1.remove_card())
    
    player2_cards = []
    player2_cards.append(player2.remove_card())
    
    #while at_war
    at_war = True
    
    while at_war:
        
        #print("We have a war!")
        
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war= False
            
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war= False
        
        else:
            print("WE HAVE A WAR!")
            
            if len(player1.allcards) <5:
                print("Player1 does not have enough cards to win this war")
                print("Player2 has won this game")
                game_on = False
                break
                
            elif len(player2.allcards) <5:
                print("Player2 does not have enough cards to win this war")
                print("Player1 has won this game")
                game_on = False
                break
            
            else:
                for x in range(5):
                    player1_cards.append(player1.remove_card())
                    player2_cards.append(player2.remove_card())
             