# Sebastian Soto
# Im am going to implement "saying uno" to the code 



import random

def start_game():
    # the setup of uno
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))

    deck = [(ranks, colour) for rank in ranks for colour in colours]

    # shuffle the deck

    random.shuffle(deck)

    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck[14:]
    
    # each player has 7 cards
    
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    # central card

    central_card = deck.pop(0)    
    
    whose_turn = p1

    # we choose how this information is encoded
    # WE DECIDE 0 = player 1, 1 = player 2 

    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):

    while p1 and p2:

        print(f"Player {whose_turn + 1}'s turn, here is your hand: {p1} ")
        print(f"\nCentral card is: {central_card}")
        
        # give the user a choice : play a card or draw a card

        if len[p1] or len[p2] == 1:
            ans = bool(input("You have a choice. You can (0) draw , (1) play, (3) call uno or (4) call out player"))
        else:
            ans = bool(input("You have a choice. You can (0) draw or (1) play"))

        if ans == 1:
            # ask the user for a card to playing
            player_choice = int(input("Which card to play?")) - 1
            
            valid = valid_play(central_card, p1[player_choice])
            if valid:
                central_card = p1.pop(player_choice)


            # the code that deals with "playing"
        if ans == 2:
            drawn_card = deck.pop(0)
            p1.append(drawn_card)
        # we will set up the data so the next loop works succesfully  
        if ans == 3:
            saying_uno = input(

        if ans == 4:
        p1, p2 = p2, p1
        whose_turn = (whose_turn + 1) % 2

        # replace player 1 hand with player 2

            # the code that deals with drawing 

def valid_play(card1, card2):
    # return true if the number or the colour of the cards in the game
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
