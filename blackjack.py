#! /usr/bin/env python3
# this is the shebang line

import logging

# Set up the debug console
logging.basicConfig(filename='blackjackLogFile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Disable the debugging

#logging.disable(logging.CRITICAL)

# Begin the program
logging.debug('Start of program')

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

dealtCards = {}

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
        logging.debug(person + '\'s hand returned is %s' % (dealtCards[person]))
        logging.debug('Cards dealt so far are %s' % (dealtCards))
    return dealtCards

first_round()

print('Your hand is: ' + str(dealtCards['player']))
print('The dealer\'s hand is a ' + str(dealtCards['dealer'][0]) + ' and a covered card')


# add up the total
import re

numberRegex = re.compile(r'\d{1,2}')
faceRegex = re.compile(r'\d{4,}')
aceRegex = re.compile(r'\d{3}')

cardRegex = re.compile(r'''

(\d{1,2} | \w{4,} | \w{3}) # Numbers or Faces or Ace
\sof\s # of part
\w{5,} # suits part

''',re.VERBOSE)

def add_up(number):
    total = 0
    for i in range(number):
        logging.debug('Adding up over %s cards in the hand' % (i+1))
        value = cardRegex.search(hand[i])
        logging.debug('Card that is being valued is %s' % (hand[i]))
        if value.group(1) in ['Jack', 'Queen', 'King']:
            numberVal = 10
        elif value.group(1) == 'Ace':
            numberVal = 1
        else:
            numberVal = int(value.group(1))
        total = total + numberVal
        logging.debug('Total after %s cards is %s' % (i+1, total))
    logging.debug('Total returned is %s' % (total))
    if total > 21:
        print('Unlucky pal, you\'re BUST!')
    return total

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

