import sys
from utils.deck import create_deck, shuffle, compare_cards
sys.path.append('C:/Users/owner/desktop/utils/deck.py')

def create_player(name = 'AI') -> dict:
    return {'name': name, 'hand': [], 'win_pile': []}

def init_game()->dict:
    player_1 = create_player(name = 'gad')
    player_2 = create_player()
    deck = create_deck()
    for _ in range(100):
        shuffle(deck)
    player_1['hand'] = deck[:27]
    player_2['hand'] = deck[27:]
    return {'deck': deck, 'player_1': player_1, 'player_2': player_2}

def play_round(p1:dict,p2:dict):
    p_1_card = p1.get('hand').pop(0)
    p_2_card = p2.get('hand').pop(0)
    result = compare_cards(p_1_card, p_2_card)
    if result == 'p1':
        p1['win_pile'].append(p_1_card)
        p1['win_pile'].append(p_2_card)
    else:
        p2['win_pile'].append(p_1_card)
        p2['win_pile'].append(p_2_card)
    return

print(init_game())