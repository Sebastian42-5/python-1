
# import necessary modules

import random
import time 


# define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
suits = ("hearts", "diamonds", "clubs", "spades")

# create a deck of cards

deck = [(suit, rank) for suit in suits for rank in ranks]

# shuffle the deck 

random.shuffle(deck)

# split the deck into two hands

player1_hand = deck[:26]

player2_hand = deck[26:]

# comparison between two cards

def card_comparison(p1_card, p2_card):
    player1_rank = ranks.index(p1_card[0])
    player2_rank = ranks.index(p2_card[0])

    if player1_rank > player2_rank:  
        return 1
    elif player2_rank < player1_rank: 
        return 2
    else :
        return 0


    """this is the logic that compares two cards to find the stronger card
		return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		hint, using the index function will make this very simple (one liner)"""
    # your code here

def play_round(player1_hand, player2_hand):
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return False 

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)

    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")

    result = card_comparison(p1_card , p2_card)

    if result == 1: 
        print("Player 1 wins this rounrd!")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)

    elif result == 2:
        print("Player 2 wins this round!")
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)

    else:
        print("there is a tie! That means war!")
        war(player_1hand, player2_hand)
    
    return True 

    """play a single round of the game.
		that is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # your code here

def war(player1_hand, player2_hand):
    for deck in range(4):

        p1_hidden_cards = p1_deck.pop(0) 
        p2_hidden_cards = p1_deck.pop(0)
    p1_war_card = p1_hidden_cards[-1]
    p2_war_card = p2_hidden_cards[-1]

    if result == 1:
       player1_hand.append(p1_war_card)
       player1_hand.append(p2_war_card)
       print("player 1 has won the war!")

    if result == 2:
       player2_hand.append(p2_war_card)
       player2_hand.append(p1_war_card)
       print("player 2 has won the war!")

    else :
        print("the war continues!")
        war(player1_hand, player2_hand)




    
    """handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. the player with the stronger
		card takes all the cards.		
	"""
    # your code here

def play_game():

    """main function to run the game."""
    # your code here
    round_count = 1
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        print(f"\nRound {round_count} :")
        if not play_round(player1_hand, player2_hand):
            break 
        round_count += 1
        time.sleep(1)


    if len(player1_hand) == 0:
        print("\nplayer 2 won the game!")
    else:
        print("\nPlayer 1 won the game!")
    print("Thanks for playing!")

# call the main function to start the game
play_game()

