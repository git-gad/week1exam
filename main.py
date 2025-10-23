from utils.deck import create_deck, shuffle, compare_cards
from game_logic.game import init_game, play_round

if __name__ == "__main__":
    game = init_game()
    while game['player_1']['hand'] and game['player_2']['hand']:
        play_round(game['player_1'], game['player_2'])
    if game['player_1']['hand'] > game['player_2']['hand']:
        print('player1 win')
    else:
        print('player2 win')
        
        
