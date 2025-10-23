import sys
from random import randint
sys.path.append('C:/Users/owner/desktop/utils/deck.py')

def create_card(rank:str,suite:str) -> dict:
    values = {'V': 11, 'Q': 12, 'K': 13, 'A': 14}
    if rank.isdigit():
        value = int(rank)
    else:
        value = values[rank]
    return {'rank': rank, 'suite': suite, 'value': value}

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    elif p2_card['value'] > p1_card['value']:
        return 'p2'
    else:
        return "WAR"
    
def create_deck() -> list[dict]:
    suits = ['H', 'C', 'D', 'S']
    ranks = ['J', 'Q', 'K', 'A']
    deck = []
    for card in range(2, 11):
        for i in range(4):
            deck.append({'rank': str(card), 'suite': suits[i], 'value': card})
    for i in range(4):
        if i == 0:
            val = 11
        elif i == 1:
            val = 12
        elif i == 2:
            val = 13
        elif i == 3:
            val = 14
        for j in range(4):
            deck.append({'rank': ranks[i], 'suite': suits[i], 'value': val})
    return deck

def shuffle(deck:list[dict]) -> list[dict]:
    index1 = randint(0, 51)
    index2 = randint(0, 51)
    while index1 == index2:
        index1 = randint(0, 51)
    deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck



