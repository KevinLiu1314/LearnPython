# -*- coding: utf-8 -*-
# Problem 54
# Poker hands

# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example
# 1 below). But if two ranks tie, for example, both players have a pair of
# queens, then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:
# Hand    Player 1            Player 2            Winner
# 1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
#         Pair of Fives       Pair of Eights
# 2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
#         Highest card Ace    Highest card Queen
# 3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
#         Three Aces          Flush with Diamonds
# 4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
#         Pair of Queens      Pair of Queens
#         Highest card Nine   Highest card Seven
# 5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
#         Full House          Full House
#         With Three Fours    with Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear
# winner.

# How many hands does Player 1 win?

from time import time
from collections import *


def rank(h):
    cards = [c[0] for c in h]
    freq = Counter(cards)
    ordered_hand = []
    for key in freq:
        ordered_hand.append((freq[key], key))
    ordered_hand = sorted(ordered_hand, reverse=True)

    if len(ordered_hand) == 5:
        straight = ordered_hand[0][1] - ordered_hand[4][1] == 4
        flush = len(set([c[1] for c in h])) == 1
        if straight and flush:
            if ordered_hand[0][1] == 14:
                r = "Royal Flush"
            else:
                r = "Straight Flush"
        elif straight:
            r = "Straight"
        elif flush:
            r = "Flush"
        else:
            r = "High Card"
    elif len(ordered_hand) == 4:
        r = "One Pair"
    elif len(ordered_hand) == 3:
        if ordered_hand[0][0] == 3:
            r = "Three of a Kind"
        else:
            r = "Two Pairs"
    else:
        if ordered_hand[0][0] == 4:
            r = "Four of a Kind"
        else:
            r = "Full House"

    cards = []
    for c in ordered_hand:
        for f in range(c[0]):
            cards.append(c[1])

    return [r, cards]


def winner(h1, h2):
    ranked1 = rank(h1)
    ranked2 = rank(h2)
    if rank_values[ranked1[0]] > rank_values[ranked2[0]]:
        return 1
    elif rank_values[ranked1[0]] == rank_values[ranked2[0]]:
        if ranked1[1] > ranked2[1]:
            return 1
        else:
            return 2
    else:
        return 2

start_time = time()

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_values = {'S': 4, 'H': 3, "C": 2, "D": 1}

rank_values = {"High Card": 1, "One Pair": 2, "Two Pairs": 3, "Three of a Kind": 4,
               "Straight": 5, "Flush": 6, "Full House": 7, "Four of a Kind": 8,
               "Straight Flush": 9, "Royal Flush": 10}

hands = []
for line in open("Problem 54.txt").readlines():
    hand1 = []
    for card in line.strip().split(" ")[:5]:
        hand1.append((card_values[card[0]], suit_values[card[1]]))
    hand2 = []
    for card in line.strip().split(" ")[-5:]:
        hand2.append((card_values[card[0]], suit_values[card[1]]))
    hands.append((hand1, hand2))

count = 0
for hand in hands:
    if winner(hand[0], hand[1]) == 1:
        count += 1

print "Answer:", count

print "Total Time: ", time() - start_time

# Completed on Mon, 14 Apr 2014, 04:19
# Solve by: 17238
# ---------------
# Answer: 376
# Total Time:  0.0460000038147
# [Finished in 0.2s]
