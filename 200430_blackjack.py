#! /usr/bin/env python3
# this is the shebang line

import logging
import random

# Set up the debug console
logging.basicConfig(filename='blackjackLogFile.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Disable the debugging

# logging.disable(logging.CRITICAL)

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

for i in range(1, 11):
    scores[str(i)] = i
logging.debug('Scores assigned are %s' % (scores))

# Setting up a dictionary to track the cards that have been thus far dealt
dealtCards = {}

# Setting up a dictionary to track the players' current scores
currentScores = {
    'player': 0,
    'dealer': 0
}

responses = {
    'yes': ['Hit', 'hit', 'Draw', 'draw', 'Twist', 'twist'],
    'no': ['Stick', 'stick', 'Stand', 'stand', 'Stay', 'stay']
}


# Randomise being given a card


def draw_card():
    suit = suits[random.randrange(4)]
    global number
    number = numbers[random.randrange(14)]
    card = str(number) + ' of ' + suit
    while card in dealtCards:
        draw_card()
    return card


# Create a RegEx for the first part of the Card

'''Randomise being given a second card,
    ensuring it cannot be the same as the first)
    '''


def first_round():
    global cardsFirstRound
    cardsFirstRound = [
                      ['playerHand', 'player1', 'player2'],
                      ['dealerHand', 'dealer1', 'dealer2']]
    for i in range(2):
        person = str(cardsFirstRound[i][0][:-4])
        logging.debug('Person assigned is %s' % (person))
        cardsFirstRound[i][1] = draw_card()
        currentScores[person] = scores[number]
        dealtCards[person] = cardsFirstRound[i][1]
        logging.debug('Cards dealt so far are %s' % (dealtCards))
        cardsFirstRound[i][2] = draw_card()
        while cardsFirstRound[i][2] in dealtCards.values():
            cardsFirstRound[i][2] = draw_card()
        cardsFirstRound[i][0] = [cardsFirstRound[i][1], cardsFirstRound[i][2]]
        dealtCards[person] = cardsFirstRound[i][1:]
        currentScores[person] += scores[number]
        logging.debug(person + '\'s hand returned is %s'
                      % (dealtCards[person]))
        logging.debug(person + '\'s hand score is %s'
                      % (currentScores[person]))
        logging.debug('Cards dealt so far are %s' % (dealtCards))
    return dealtCards


first_round()

print('Your hand is: ' + dealtCards['player'][0] +
      ' and ' + dealtCards['player'][1])
print('The dealer\'s hand is a ' + str(dealtCards['dealer'][0]) +
      ' and a covered card')


# add up the total
'''
def add_up(number):
    for n in currentScores.keys():
        logging.debug('Person assigned is %s' % (n))
        startScore = currentScores[n]
        for i in range(number):
            currentScores[n] = currentScores[n] + scores[dealtCards[n][i][0]]
        logging.debug('%s score is %s' % (n, currentScores[n]))

add_up(2)
'''
# ask them what they want to do next


def ask_next(turn):
    offerQuestion = 'What would you like to do now? '
    nextMove = input(offerQuestion)
    if nextMove in responses['no']:
        finalHand = dealtCards['player']
        finalScore = currentScores['player']
        print('Your hand is: ' + str(finalHand))
        print('Your final score is: ' + str(finalScore))
    elif nextMove in responses['yes']:
        print('Okay. Dealing an extra card...')
        dealtCards['player'].append(draw_card())
        currentScores['player'] += scores[number]
        print('You drew a ' + dealtCards['player'][turn])
        print('You hand is now ' + str(dealtCards['player']) +
              ' with a value of ' + str(currentScores['player']))
        if currentScores['player'] > 21:
            print('Aw shit! You\'re bust!')
        else:
            ask_next(turn + 1)
    else:
        print('Sorry, that\'s not a recognised response. Try again.')
        nextMove = input(offerQuestion)


turnNumber = len(dealtCards['player'])

ask_next(turnNumber)

# TODO: Decide what the computer has to do

# TODO: show the odds of stick or hit for you
