ROWS, COLS = 4, 5
PLAYER_SYMBOLS = ["X", "O", "A"]

board = [["." for _ in range(COLS)] for _ in range(ROWS)]
penalty_points = {symbol: 0 for symbol in PLAYER_SYMBOLS}

def print_board():
    for row in board:
        print(" ".join(row))
    print()

def is_valid_move(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "."

def calculate_penalty(symbol, row, col):
    penalties = 0
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == symbol:
            penalties += 1
    return penalties

def play_game():
    total_moves = ROWS * COLS
    for turn in range(total_moves):
        print_board()
        symbol = PLAYER_SYMBOLS[turn % 3]
        print(f"Ход игрока {turn % 3 + 1} ({symbol}).")

        while True:
            try:
                row, col = int(input("Строка (0-3): ")), int(input("Столбец (0-4): "))
                if is_valid_move(row, col):
                    break
                print("Некорректный ход. Попробуйте еще раз.")
            except ValueError:
                print("Введите числа для строки и столбца.")

        board[row][col] = symbol
        penalty_points[symbol] += calculate_penalty(symbol, row, col)

    print_board()
    print("Игра завершена!")
    for symbol, points in penalty_points.items():
        print(f"Игрок {PLAYER_SYMBOLS.index(symbol) + 1} ({symbol}) - штрафные очки: {points}")

    min_points = min(penalty_points.values())
    winners = [PLAYER_SYMBOLS.index(s) + 1 for s, p in penalty_points.items() if p == min_points]
    if len(winners) > 1:
        print(f"Ничья между игроками: {', '.join(map(str, winners))}")
    else:
        print(f"Победил игрок {winners[0]} с {min_points} штрафными очками.")

# Запуск игры
play_game()
