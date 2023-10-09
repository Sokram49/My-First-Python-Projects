''' Simple Blackjack Card Game '''

import itertools
import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = list(itertools.product(ranks, suits))
random.shuffle(deck)

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

def calc_hand_value(hand):
    total_value = 0
    num_aces = 0

    for card in hand:
        rank, _ = card
        total_value += card_values[rank]
        if rank == 'Ace':
            num_aces += 1

    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

def display_hands(player_hand, dealer_hand):
    print(f"Player's Hand: {player_hand}, Total:, {calc_hand_value(player_hand)}")
    print(f"Dealer's Hand: {dealer_hand}, Total:, {calc_hand_value(dealer_hand)}")

def is_blackjack(hand):
    return len(hand) == 2 and calc_hand_value(hand) == 21

while True:
    display_hands(player_hand, dealer_hand)
    if is_blackjack(player_hand):
        print("Player has Blackjack!")
        if is_blackjack(dealer_hand):
            print("Dealer also has Blackjack. It's a push.")
        else:
            print("Player wins with Blackjack!")
        break

    while True:
        option = input("What would you like to do? (Hit/Stand): ").lower()
        if option == "hit":
            player_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand)
            if calc_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                break
        elif option == "stand":
            break

    while calc_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hands(player_hand, dealer_hand)
        if calc_hand_value(dealer_hand) > 21:
            print("Dealer busts! Player wins.")
            break
    
    player_total = calc_hand_value(player_hand)
    dealer_total = calc_hand_value(dealer_hand)
    if player_total > 21:
        print("Player busts! Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busts! Player wins.")
    elif player_total == dealer_total:
        print("It's a push.")
    elif player_total > dealer_total:
        print("Player wins!")
    else:
        print("Dealer wins.")
    replay = input("Would you like to play again? (y/n): ")
    if replay == "y":
        random.shuffle(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        continue
    else:
        print("Thank you for playing.")
        break
