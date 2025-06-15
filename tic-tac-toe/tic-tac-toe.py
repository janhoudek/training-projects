from random import randint, choice

# set basic variables
FIELD_SIZE = 3

def create_game_field() -> list[list[str]]:
    """
    Creates a game field for Tic-Tac-Toe.

    Returns:
        list[list[str]]: A 3x3 game field initialized with '-'.
    """
    game_field = []
    for i in range(FIELD_SIZE):
        row = []
        for j in range(FIELD_SIZE):
            row.append('-')
        game_field.append(row)
    return game_field

def set_player_symbol() -> str:
    """
    Sets the symbol for the player.

    Returns:
        str: The symbol chosen by the player (X or O).
    """

    symbol_player = input('Please, choose your symbol (X/O): ')
    symbol_player = symbol_player.upper()

    while symbol_player not in ['X', 'O']:
        symbol_player = input('You entered an invalid symbol. Please, repeat the entry (X/O): ')

    return symbol_player

def field_occupancy_check(game_field: list[list[str]], row_index: int, column_index: int) -> bool:
    """
    Checks if a field in the game field is free.

    Args:
        game_field (list[list[str]]): The current game field.
        row_index (int): The row index to check.
        column_index (int): The column index to check.

    Returns:
        bool: True if the field is free, False otherwise.
    """

    if game_field[row_index][column_index] == '-':
        field_is_free = True
    else:
        field_is_free = False

    return field_is_free

def player_turn(symbol_player: str, game_field: list[list[str]], repeat_turn: bool = True):
    """
    Handles the player's turn.

    Args:
        symbol_player (str): The symbol of the player (X or O).
        game_field (list[list[str]]): The current game field.
        repeat_turn (bool, optional): Whether to repeat the turn if the field is occupied. Defaults to True.
    """

    row_player, column_player = input('Enter row number and column number: ').split()

    while repeat_turn:
        row_player = int(row_player) - 1
        column_player = int(column_player) - 1

        if field_occupancy_check(game_field, row_player, column_player):
            game_field[row_player][column_player] = symbol_player
            repeat_turn = False
        else:
            row_player, column_player = input('The field is taken, enter new values: ').split()

def computer_turn(symbol_computer: str, game_field: list[list[str]]):
    """
    Handles the computer's turn.

    Args:
        symbol_computer (str): The symbol of the computer (X or O).
        game_field (list[list[str]]): The current game field.
    """

    row_computer = randint(0, 2)
    column_computer = randint(0, 2)

    repeat_turn = True

    while repeat_turn:
        if field_occupancy_check(game_field, row_computer, column_computer):
            game_field[row_computer][column_computer] = symbol_computer
            repeat_turn = False
        else:
            row_computer = randint(0, 2)
            column_computer = randint(0, 2)

def on_turn(active_symbol: str) -> str:
    """
    Determines the active player based on the current symbol.

    Args:
        active_symbol (str): The symbol of the active player (X or O).

    Returns:
        str: The name of the active player ('PLAYER' or 'COMPUTER').
    """
    if active_symbol == symbol_player:
        active_player = 'PLAYER'
    else:
        active_player = 'COMPUTER'

    return active_player

def draw_check(game_field: list[list[str]], game_in_progress: bool) -> bool:
    """
    Checks for a draw condition in the game.

    Args:
        game_field (list[list[str]]): The current game field.
        game_in_progress (bool): The current state of the game.

    Returns:
        bool: The updated state of the game (True if still in progress, False if drawn).
    """

    free_fields = len(game_field)**2

    for row in game_field:
        for field in row:
            if field != '-':
                free_fields -= 1

    if free_fields == 0:
        message = 'All fields occupied, game ends in a DRAW.'
        game_in_progress = False
        print(message)
    else:
        pass

    return game_in_progress

def win_check(active_symbol: str, field: list[list[str]], game_in_progress: bool) -> bool:
    """
    Checks for a win condition in the game.

    Args:
        active_symbol (str): The symbol of the active player (X or O).
        field (list[list[str]]): The current game field.
        game_in_progress (bool): The current state of the game.

    Returns:
        bool: The updated state of the game (True if still in progress, False if won).
    """

    # row check
    for row in range(FIELD_SIZE):
        if field[row][0] == field[row][1] == field[row][2]==active_symbol:
            message = f'{on_turn(active_symbol)} wins!'
            game_in_progress = False

    # column check
    for column in range(FIELD_SIZE):
        if field[0][column] == field[1][column] == field[2][column] == active_symbol:
            message = f'{on_turn(active_symbol)} wins!'
            game_in_progress = False

    # diagonals check
    if field[0][0] == field[1][1] == field[2][2] == active_symbol:
        message = f'{on_turn(active_symbol)} wins!'
        game_in_progress = False

    if field[0][2] == field[1][1] == field[2][0] == active_symbol:
        message = f'{on_turn(active_symbol)} wins!'
        game_in_progress = False

    if game_in_progress == False:
        print(message)
    else:
        pass

    return game_in_progress

def print_field(field: list[list[str]]):
    """
    Prints the current game field.

    Args:
        field (list[list[str]]): The current game field.
    """

    for item in field:
        print(item)

def on_turn_change(active_symbol: str) -> str:
    """
    Changes the active player symbol.

    Args:
        active_symbol (str): The symbol of the active player (X or O).

    Returns:
        str: The symbol of the next player (X or O).
    """
    global symbol_player, symbol_computer
    
    if active_symbol == symbol_player:
        active_symbol = symbol_computer
    else:
        active_symbol = symbol_player

    return active_symbol

if __name__ == '__main__':

    game_in_progress = True

    print('Welcome to the game TIC-TAC-TOE.')

    # create game field
    game_field = create_game_field()

    # choose symbol
    symbol_player = set_player_symbol()

    # nastav symbol pro počítač
    if symbol_player == 'X':
        symbol_computer = 'O'
    else:
        symbol_computer = 'X'

    # determination of a beginning player
    active_symbol = choice([symbol_player, symbol_computer])

    # game
    while game_in_progress:

        print(f'{on_turn(active_symbol)} is on turn. ({active_symbol})')

        # turn
        if active_symbol == symbol_player:
            player_turn(active_symbol, game_field)

        elif active_symbol == symbol_computer:
            computer_turn(active_symbol, game_field)

        # print game field
        print_field(game_field)

        # win check
        game_in_progress = win_check(active_symbol, game_field, game_in_progress)

        if game_in_progress:
            pass
        else:
            break

        # draw check
        game_in_progress = draw_check(game_field, game_in_progress)
        
        # change turn
        active_symbol = on_turn_change(active_symbol)              