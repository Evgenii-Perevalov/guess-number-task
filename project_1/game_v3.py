"""Игра угадай число
Компьютер сам загадывает и сам угадывает число с минимальным количеством попыток
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Угадываем число с мимнимальным количеством попыток.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = []
    
    def count_number(selection):
        count.append(1)
        # середина выборки
        middle_number = (selection[-1]-selection[0])//2 + selection[0]
        
        if number == middle_number:
            result = len(count)
            return result # завершение функции при угадывании числа
        elif number < middle_number:
            # делим выборку на 2 части и рассматриваем ту, где наше число
            return count_number(list(range(selection[0],middle_number+1)))
        else:
            return count_number(list(range(middle_number+1,selection[-1]+1)))
    
    result = count_number(list(range(1,101)))
    return result


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)