import Card from ./Class/cards.py
import Deck from ./Class/deck.py
import player from ./Class/player.py

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

player1= PLayer('Player1')
player2= PLayer('PLayer2')

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
             