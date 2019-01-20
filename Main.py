class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(game):
    if len(game) > 2:
        raise WrongNumberOfPlayersError('There are too many player for the game')

    valid_moves = ['R', 'P', 'S']
    for playerMove in game:
        if not isinstance(playerMove[1], str) or playerMove[1].upper() not in valid_moves:
            raise NoSuchStrategyError('Please make a valid move')

    player_one = game[0]
    player_one_move = player_one[1]

    player_two = game[1]
    player_two_move = player_two[1]

    player_one_winner = False
    if player_one_move == player_two_move:
        player_one_winner = True
    elif player_one_move == 'R' and player_two_move == 'S':
        player_one_winner = True
    elif player_one_move == 'S' and player_two_move == 'P':
        player_one_winner = True
    elif player_one_move == 'P' and player_two_move == 'R':
        player_one_winner = True

    if player_one_winner:
        print(f'{player_one[0]} is the winner!!')
        return player_one
    else:
        print(f'{player_two[0]} is the winner!!')
        return player_two


def is_move(move):
    return len(move) == 2 and isinstance(move[0], str) and isinstance(move[1], str)


def rps_tournament_winner(games):
    try:
        return rps_game_winner(games)
    except NoSuchStrategyError:
        return rps_tournament_winner([rps_tournament_winner(games[0]), rps_tournament_winner(games[1])])


rps_game_winner([["Armando", "P"], ["Dave", "S"]])

rps_tournament_winner(
    [
        [
            [["Armando", "P"], ["Dave", "S"]],
            [["Richard", "R"], ["Michael", "S"]],
        ],
        [
            [["Allen", "S"], ["Omer", "P"]],
            [["David E.", "R"], ["Richard X.", "P"]],
        ],
    ])
