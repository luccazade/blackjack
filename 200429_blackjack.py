#! /usr/bin/env python3
# this is the shebang line

import logging

# Set up the debug console
logging.basicConfig(filename='blackjackLogFile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Disable the debugging

#logging.disable(logging.CRITICAL)

# Begin the program
logging.debug('****Start of program****')

# Blackjack odds

# list out all the 52 cards in a Python friendly way

suits = {
    0: 'Hearts',
    1: 'Clubs',
    2: 'Diamonds',
    3: 'Spades'
    }

numbers = {
    0: 'Ace',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
    }

scores = {
    'Ace': 1,
    'King': 10,
    'Queen': 10,
    'Jack': 10
}

for i in range(1,11):
    scores[str(i)] = i
logging.debug('Scores assigned are %s' % (scores))

dealtCards = {}
currentScores = {
    'player': 0,
    'dealer': 0
}

# Randomise being given a card

import random, re

def draw_card():
    suit = suits[random.randrange(4)]
    number = numbers[random.randrange(14)]
    card = str(number) + ' of ' + suit
    return card

# Randomise being given a second card, ensuring it cannot be the same as the first

def first_round():
    global cardsFirstRound
    cardsFirstRound = [['playerHand', 'playerFirst', 'playerSecond'], ['dealerHand', 'dealerFirst', 'dealerSecond']]
    for i in range(2):
        person = str(cardsFirstRound[i][0][:-4])
        logging.debug('Person assigned is %s' % (person))
        cardsFirstRound[i][1] = draw_card()
        dealtCards[person] = cardsFirstRound[i][1]
        logging.debug('Cards dealt so far are %s' % (dealtCards))
        cardsFirstRound[i][2] = draw_card()
        while cardsFirstRound[i][2] in dealtCards.values():
            cardsFirstRound[i][2] = draw_card()
        cardsFirstRound[i][0] = [cardsFirstRound[i][1], cardsFirstRound[i][2]]
        dealtCards[person] = cardsFirstRound[i][1:]
        currentScores[person] = scores[dealtCards[person][0][0]] + scores[dealtCards[person][1][0]]
        logging.debug(person + '\'s hand returned is %s' % (dealtCards[person]))
        logging.debug(person + '\'s hand score is %s' % (currentScores[person]))
        logging.debug('Cards dealt so far are %s' % (dealtCards))
    return dealtCards

first_round()

print('Your hand is: ' + dealtCards['player'][0] + ' and ' + dealtCards['player'][1])
print('The dealer\'s hand is a ' + str(dealtCards['dealer'][0]) + ' and a covered card')


# add up the total

def add_up(number):
    for n in currentScores.keys():
        logging.debug('Person assigned is %s' % (n))
        startScore = currentScores[n]
        for i in range(number):
            currentScores[n] = currentScores[n] + scores[dealtCards[n][i][0]]
        logging.debug('%s score is %s' % (n, currentScores[n]))

add_up(2)

# ask them what they want to do next

def ask_next():
    offerQuestion = 'What would you like to do now: stick or twist? '
    nextMove = input(offerQuestion)
    if nextMove == ('stick' or 'Stick'):
        finalHand = hand
        print('Okay. Your final hand is: ' + str(hand))
    elif nextMove == ('twist' or 'Twist'):
        print('Okay')
    else:
        print('Sorry, that\'s not one of the options. Try again.')
        nextMove = input(offerQuestion)
        
ask_next()
# TODO: randomise the computer being given 2 cards, only one of which is shown
import re

dealerRegex = re.compile(r'''
('.*'),\s('.*')
''')

def dealers_hand(roundNo):
    hand()
    #if roundNo == 0:
        # substitute in the second group with 'HIDDEN'
        

# TODO: Decide what the computer has to do

# TODO: show the odds of stick or hit for you

