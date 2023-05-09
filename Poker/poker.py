import contextlib
import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "Nine", ten: "Ten", jack: "Jack", queen: "Queen", king: "King", ace: "Ace"}

player_score = 0
computer_score = 0

def roll(roll_number):
    numbers = list(range(1, 7)) #No lo toma, en la linea 77, aunque sea lista
    dice = range(roll_number)
    iterations = 0
    while iterations < roll_number:
        iterations += 1
        dice[iterations - 1] = random.choice(numbers) #TypeError: 'range' object does not support item assignment. Tiene que obtener el valor de una lista, fijarse en la linea 72 para cambiar el tipo de variable y que la tome.
    return dice

    
def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print ("Dice", i + 1, ":", dice[i])
        
    result = hand(dice)
    print ("You currently have", names[result])

    while True:
        rerolls = int(input("How many dice do you want to throw again?"))
        with contextlib.suppress(ValueError):
            if rerolls in {1, 2, 3, 4, 5}:
                break
        print ("Oops! I didn't understand that. Please enter 1, 2, 3, 4, or 5.")

    if rerolls != 0:
        result = _extracted_from_throws_(rerolls, dice)
    print ("You finish with", names[result])


# TODO Rename this here and in `throws`
def _extracted_from_throws_(rerolls, dice):
    roll_number = rerolls
    dice_rerolls = roll(roll_number)
    dice_changes = range(rerolls)
    print ("Enter the number of a dice to reroll: ")
    iterations = 0
    while iterations < rerolls:
        iterations += 1
        while True:
            selection = int(input())
            with contextlib.suppress(ValueError):
                if selection in {1, 2, 3, 4, 5}:
                    break
            print ("Oops! I didn't understand that. Please enter 1, 2, 3, 4, or 5.")
        dice_changes[iterations - 1] = selection - 1
        print ("Dice", selection, ":", dice_rerolls[iterations - 1])

    iterations = 0

    while iterations < rerolls:
        iterations += 1
        replacement = dice_changes[iterations - 1]
        dice[dice_changes[iterations - 1]] = replacement

    return _extracted_from_throws_(dice)


# TODO Rename this here and in `throws`
def _extracted_from_throws_(dice):
    dice.sort()
    for i in range(len(dice)):
        print ("Dice", i + 1, ":", dice[i])
    return hand(dice)


def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice in [straight1, straight2]:
        return straight2

    elif dice_hand[0] == 5:
        return five

    elif dice_hand[0] == 4:
        return four

    elif dice_hand[0] == 3:
        return full_house if dice_hand[1] == 2 else three
    elif dice_hand[0] == 2:
        return two_pair if dice_hand[1] == 2 else one_pair
    else:
        return nine

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print ("Thank you very much for playing our game. See you next time!")
        
def scores():
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("Player: ", player_score)
    print ("Computer: ", computer_score)

def game():
    print ("The computer will help you to pick a card.")
    throws()
    return play_again()

def start():
    print ("Let's play a game of Linux Poker.")
    while game():
        pass
    scores()

if __name__ == '__main__':
    start()