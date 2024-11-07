
ROWS = 4
COLS = 5

PLAYER_SYMBOLS = ["X", "O", "A"]

board = [["." for _ in range(COLS)] for _ in range(ROWS)]
penalty_points = {symbol: 0 for symbol in PLAYER_SYMBOLS}


def print_board():
    for row in board:
        print(" ".join(row))
    print()


def is_valid_move(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "."


def count_penalty(symbol, row, col):
    penalties = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Верхние соседи
        (0, -1), (0, 1),  # Левые и правые соседи
        (1, -1), (1, 0), (1, 1)  # Нижние соседи
    ]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == symbol:
            penalties += 1
    return penalties


def play_game():
    turn = 0
    total_moves = ROWS * COLS

    while turn < total_moves:
        print_board()
        current_player = turn % 3
        symbol = PLAYER_SYMBOLS[current_player]
        print(f"Ход игрока {current_player + 1} ({symbol}).")

        while True:
            try:
                row = int(input("Введите номер строки (0-3): "))
                col = int(input("Введите номер столбца (0-4): "))
                if is_valid_move(row, col):
                    break
                else:
                    print("Некорректный ход, выберите пустую клетку.")
            except ValueError:
                print("Пожалуйста, введите числовые координаты.")

        board[row][col] = symbol
        penalties = count_penalty(symbol, row, col)
        penalty_points[symbol] += penalties
        print(f"Штрафные очки за этот ход: {penalties}")

        turn += 1

    print_board()
    print("Игра завершена!")
    for symbol in PLAYER_SYMBOLS:
        print(f"Игрок {PLAYER_SYMBOLS.index(symbol) + 1} ({symbol}) набрал {penalty_points[symbol]} штрафных очков.")

    winner = min(penalty_points, key=penalty_points.get)
    min_points = penalty_points[winner]
    winners = [s for s, p in penalty_points.items() if p == min_points]

    if len(winners) > 1:
        print("Игра окончилась ничьей между игроками:",
              ", ".join([f"{PLAYER_SYMBOLS.index(w) + 1} ({w})" for w in winners]))
    else:
        print(f"Победил игрок {PLAYER_SYMBOLS.index(winner) + 1} ({winner}) с {min_points} штрафными очками.")


play_game()
