
# Import necessary modules
import random
import time 

time.sleep(1)

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards

deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck 

random.shuffle(deck)

# Split the deck into two hands

p1_deck = deck[:26]

p2_deck = deck[26:]

p1_card = p1_deck.pop(0)
p2_card = p2_deck.pop(0)


def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]): 
        print("Player 1 has a stronger card! They win!") 
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        print("Player 2 has a stronger card! They win!") 
        return 2
    else :
        return 0


    """this is the logic that compares two cards to find the stronger card
		return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		hint, using the index function will make this very simple (one liner)"""
    # your code here

def play_round(player1_hand, player2_hand):
    
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)
    
    result = card_comparison(p1_card , p2_card)

    if result == 1: 
        p1_deck.append(p1_card)
        p1_deck.append(p2_card)

    if result == 2:
        p2_deck.append(p2_card)
        p2_deck.append(p1_card)

    else:
        print("There is a tie! That means War!")
        war(player_1hand, player_hand)

    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    for deck in range(4):

        p1_hidden_cards = p1_deck.pop(0) 
        p2_hidden_cards = p1_deck.pop(0)
    p1_war_card = p1_hidden_cards[-1]
    p2_war_card = p2_hidden_cards[-1]

    if result == 1:
       p1_deck.append(p1_war_card)
       p1_deck.append(p2_war_card)
    
    if result == 2:
       p2_deck.append(p2_war_card)
       p1_deck.append(p1_war_card)
    else :
        print("The war continues!")
        war(player1_hand, player2_hand)




    
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():


    
    """Main function to run the game."""
    # Your code here


def gameloop():
    while len(p1_deck) > 0 and len(p2_deck) > 0:
            

# Call the main function to start the game
play_game()

