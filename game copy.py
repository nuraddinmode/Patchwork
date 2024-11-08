# Константы
ROWS, COLS = 4, 5  # Устанавливаю количество строк и столбцов для игрового поля
PLAYER_SYMBOLS = ["X", "O", "A"]  # определяю символы для каждого из трех игроков

# Инициализация поля и счетчиков штрафных очков
board = [["." for _ in range(COLS)] for _ in range(ROWS)]  # создаю пустое игровое поле 4x5
penalty_points = {symbol: 0 for symbol in PLAYER_SYMBOLS}  # создаю словарь для подсчета штрафных очков каждого игрока

def print_board():
    # вывожу текущее состояние игрового поля на экран
    for row in board:
        print(" ".join(row))  # печатаю каждую строку поля
    print()  # добавляю пустую строку для разделения

def is_valid_move(row, col):
    # проверяю, допустим ли ход — находится ли клетка в пределах поля и пуста ли она
    return 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "."

def calculate_penalty(symbol, row, col):
    penalties = 0  # начинаю с нуля штрафных очков
    # перебираю все восемь соседних клеток (вверх, вниз, влево, вправо и по диагоналям)
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nr, nc = row + dr, col + dc  # вычисляю координаты соседней клетки
        # проверяю, находится ли соседняя клетка в пределах поля и содержит ли символ текущего игрока
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == symbol:
            penalties += 1  # увеличиваю количество штрафных очков на 1, если условия выполняются
    return penalties  # возвращаю общее количество штрафных очков для данного хода

def play_game():
    total_moves = ROWS * COLS  # вычисляю общее количество ходов, чтобы игра закончилась при заполнении поля
    for turn in range(total_moves):
        print_board()  # вывожу текущее состояние поля на каждом ходе
        symbol = PLAYER_SYMBOLS[turn % 3]  # определяю текущего игрока, чередуя символы по кругу
        print(f"Ход игрока {turn % 3 + 1} ({symbol}).")  # вывожу сообщение о текущем игроке

        # Получение и проверка хода
        while True:
            try:
                row, col = int(input("Строка (0-3): ")), int(input("Столбец (0-4): "))  # запрашиваю строку и столбец
                if is_valid_move(row, col):  # проверяю, допустим ли ход
                    break  # Если ход допустим, я выхожу из цикла while
                print("Некорректный ход. Попробуйте еще раз.")  # Если ход недопустим, я вывожу предупреждение
            except ValueError:
                print("Введите числа для строки и столбца.")  # Если ввод некорректный, я вывожу сообщение об ошибке

        # Обновление состояния игры
        board[row][col] = symbol  # записываю символ игрока в выбранную клетку
        penalty_points[symbol] += calculate_penalty(symbol, row, col)  # добавляю к штрафным очкам игрока штрафы

    # Конец игры
    print_board()  # вывожу финальное состояние поля
    print("Игра завершена!")  # вывожу сообщение об окончании игры
    for symbol, points in penalty_points.items():
        # вывожу количество штрафных очков для каждого игрока
        print(f"Игрок {PLAYER_SYMBOLS.index(symbol) + 1} ({symbol}) - штрафные очки: {points}")

    # Определение победителя
    min_points = min(penalty_points.values())  # нахожу минимальное количество штрафных очков среди игроков
    winners = [PLAYER_SYMBOLS.index(s) + 1 for s, p in penalty_points.items() if p == min_points]
    # создаю список победителей. Если несколько игроков набрали одинаковое минимальное количество очков, их всех добавляю в список победителей.
    if len(winners) > 1:
        # Если в списке `winners` больше одного игрока, я объявляю ничью
        print(f"Ничья между игроками: {', '.join(map(str, winners))}")
    else:
        # Если победитель один, я вывожу сообщение о его победе
        print(f"Победил игрок {winners[0]} с {min_points} штрафными очками.")

# Запуск игры
play_game()  # вызываю основную функцию игры для начала игрового процесса

