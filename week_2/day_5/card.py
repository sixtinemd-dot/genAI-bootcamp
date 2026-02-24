from daily_challenge_25 import Deck

deck = Deck()
print(deck) 
deck.build()
print(deck)        
deck.shuffle()
card = deck.deal()
print("Card dealt:", card)
print(deck)  