
# assumptions: infinite deck (cards are not removed), the cards represented are on a list, no jokers, face cars are 10, ace is either 11 or 1,
# equal probability for all cards

import random

def change_ace(hand):
    """changing aces from 11 to 1"""
    index=0
    for card in hand:
        if card==11: #if card is an ace
            hand[index]=1
        index+=1

def is_under_17(hand):
    """checking if a hand is smaller than 17"""
    sum=0
    for card in hand:
        sum+=card
    if sum>=17:
        return False
    else:
        return True
    
def is_over_21(hand):
    """checking if a hand is bigger than 21"""
    sum=0
    for card in hand: #calculate inital sum
        sum+=card
    if sum>21:
        change_ace(hand) #if higher than 21 and there is ace it will change it
        sum=0 #check new sum
        for card in hand:
            sum+=card
        if sum>21:
            return True
        else:
            return True
    else:
        return False
def deal_card(hand):
    """deal a new random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #deck of cards
    hand.append(cards[random.randint(0,12)]) #deal a random card

def validate_input(input):
    """checks if an input is valid"""
    input.lower()
    if input=='y' or input =='n': #valid input
        return True
    else:
        return False
    
def comparing_hands(user_hand,dealer_hand):
    """compare hands and print winning statement"""
    print_final_state(user_hand,dealer_hand)
    dealer_sum=0
    user_sum=0
    #summing hands
    for card in user_hand: 
        user_sum+=card
    for card in dealer_hand:
        dealer_sum+=card
    if user_sum>dealer_sum:
        print("User win!")
    elif user_sum<dealer_sum:
        print("Dealer win!")
    else:
        print("Draw!")

def print_final_state(user_hand,dealer_hand):
    """printing the final state"""
    print(f"User hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")

def print_state(user_hand,dealer_hand):
    """printing the current state"""
    print(f"Your cards: {user_hand}")
    print(f"Dealer's first card: {dealer_hand[0]}")



user_hand = []
dealer_hand = []
for i in range(0,2):
    deal_card(user_hand)
    deal_card(dealer_hand)
print_state(user_hand,dealer_hand)

play = True
while play:
    #user turn
    choice=input("Type 'y' to get another card, type 'n' to pass: ")
    if not validate_input(choice):
        print("Invalid input")
        continue
    if choice.lower()=='y':
        deal_card(user_hand)
        if is_over_21(user_hand):
            if is_over_21(user_hand):
                print(f"Your hand is: {user_hand}\nYou went over 21, you lose.")
                play = False
                break
        print_state(user_hand,dealer_hand)
        continue
    else: #dealer "turn"
        while(is_under_17(dealer_hand)):
            deal_card(dealer_hand)
        if is_over_21(dealer_hand):
            print_final_state(user_hand,dealer_hand)
            print("Dealer went over 21, You win!")
            break
        else:
            comparing_hands(user_hand,dealer_hand)
            break