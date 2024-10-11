
# import necessary modules

import random
import time 


# define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
suits = ("hearts", "diamonds", "clubs", "spades")

# create a deck of cards

deck = [(rank, suit) for rank in ranks for suit in suits]

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

    print(f"Player 1 plays: {p1_card[0]} of {p1_card[1]}, Player 2 plays: {p2_card[0]} of {p2_card[1]}")

    result = card_comparison(p1_card , p2_card)

    if result == 1: 
        print("Player 1 wins this round!")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)

    elif result == 2:
        print("Player 2 wins this round!")
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)

    else:
        print("There is a tie! That means war!")
        war(player1_hand, player2_hand)
    
    return True 

    """play a single round of the game.
		that is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # your code here

def war(player1_hand, player2_hand):
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        print("Not enough cards for war! It's the end of the game...")
        return 
    player1_hidden_cards = []
    player2_hidden_cards = []

    for deck in range(3):
        if player1_hand:
            player1_hidden_cards.append(player1_hand.pop(0))
        if player2_hand: 
            player2_hidden_cards.append(player2_hand.pop(0)) 
    
    player1_war_card = player1_hand.pop(0)
    player2_war_card = player2_hand.pop(0)

    
    print(f"\nPlayer 1 plays: {player1_war_card[0]} of {player1_war_card[1]}, Player 2 plays: {player2_war_card[0]} of {player2_war_card[1]}")
    
    result = card_comparison(player1_war_card, player2_war_card)
    
    
    if result == 1:
        player1_hand.extend(player1_hidden_cards + player2_hidden_cards + [player1_war_card + player2_war_card])
        print("Player 1 has won the war!")

    if result == 2:
        player2_hand.extend(player1_hidden_cards + player2_hidden_cards + [player1_war_card + player2_war_card])        
        print("Player 2 has won the war!")

    else :
        print("The war continues!")
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
    # If one of the players runs out of cards, the game ends
        round_count += 1
        time.sleep(1)
    # This is to slow the process of the game

    if len(player1_hand) == 0:
        print("\nplayer 2 won the game!")
    else:
        print("\nPlayer 1 won the game!")
    print("Thanks for playing!")

# call the main function to start the game
play_game()

