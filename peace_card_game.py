# import necessary modules

import random
import time 

# Define the ranks and suits

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
suits = ("hearts", "diamonds", "clubs", "spades")

# Comparison between two cards

def card_comparison(p1_card, p2_card):
    player1_rank = ranks.index(p1_card[0])
    player2_rank = ranks.index(p2_card[0])

    if player1_rank > player2_rank:  
        return 1
    elif player1_rank < player2_rank: 
        return 2
    else:
        return 0

# War function

def war(player1_hand, player2_hand):
    if len(player1_hand) < 4 or len(player2_hand) < 4:
        print("Not enough cards for war! It's the end of the game...")
        return 
# These are the hidden cards

    player1_hidden_cards = [player1_hand.pop(0) for _ in range(3)]
    player2_hidden_cards = [player2_hand.pop(0) for _ in range(3)]

    player1_war_card = player1_hand.pop(0)
    player2_war_card = player2_hand.pop(0)
    
    print(f"\nPlayer 1 plays: {player1_war_card[0]} of {player1_war_card[1]}, Player 2 plays: {player2_war_card[0]} of {player2_war_card[1]}")
    
    result = card_comparison(player1_war_card, player2_war_card)
    
    if result == 1:
        player1_hand.extend(player1_hidden_cards + player2_hidden_cards + [player1_war_card, player2_war_card])
        print("Player 1 has won the war!")

    elif result == 2:
        player2_hand.extend(player1_hidden_cards + player2_hidden_cards + [player1_war_card, player2_war_card])
        print("Player 2 has won the war!")

    else:
        print("The war continues!")
        war(player1_hand, player2_hand)

# play round function

def play_round(player1_hand, player2_hand):
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return False 
    

# The game ends if it returns False

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)

    print(f"Player 1 plays: {p1_card[0]} of {p1_card[1]}, Player 2 plays: {p2_card[0]} of {p2_card[1]}")

    result = card_comparison(p1_card, p2_card)

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

# main function to call the game

def play_game():
    # Create a deck of cards
    deck = [(rank, suit) for rank in ranks for suit in suits]
    
    # Shuffle the deck 
    random.shuffle(deck)

    # Split the deck into two hands
    player1_hand = deck[:26]
    player2_hand = deck[26:]
    
    # Start of the round
    round_count = 1


    while len(player1_hand) > 0 and len(player2_hand) > 0:
    # while both players still have cards 

        print(f"\nRound {round_count}:")
        if not play_round(player1_hand, player2_hand):
            break 
        round_count += 1
        time.sleep(1)  # This is to slow the process of the game
    
# If one of the players runs out of cards, the other wins 

    if len(player1_hand) == 0:
        print("\nPlayer 2 won the game!")
    else:
        print("\nPlayer 1 won the game!")
    print("Thanks for playing!")

# Call the main function to start the game
play_game()


