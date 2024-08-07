# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
    hand_value = 0
    i = 0
    while i < 2:
        card = randint(1, 13)
        card_name = draw(card)
        print(f"{card_name}")
        hand_value += card_value(card)
        i += 1

    while hand_value < 21:
        choose = input(f"You have {hand_value}. Hit (y/n)? ")
        if choose == "y" or choose == "yes":
            card = randint(1, 13)
            card_name = draw(card)
            print(f"{card_name}")
            hand_value += card_value(card)
        elif choose == "n" or choose == "no":
            break
        else:
            print("Sorry I didn't get that.")
            continue

    if hand_value == 21:
        handvaluename = blackjack_or_bust(hand_value)
        print("Final hand: 21.")
        print(handvaluename)
    elif hand_value > 21:
        handvaluename = blackjack_or_bust(hand_value)
        print(f"Final hand: {hand_value}.")
        print(handvaluename)
    else:
        print(f"Final hand: {hand_value}.")
play_human_turn()
