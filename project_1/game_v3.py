"""Игра угадай число
Компьютер сам загадывает и сам угадывает число с минимальным количеством попыток
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Угадываем число с мимнимальным количеством попыток.
    
    Комментарий. Можно было выбрать алгоритм деления выборки подбора случайных
    чисел на 2 при каждой попытке, но интереснее было написать рекурсию с
    уменьшением выборки, чтобы условие больше/меньше в полной мере выполнялось
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = []
    
    def count_number(number_from, number_to):
        count.append(1)
        # предполагаемое число
        predict_number = np.random.randint(number_from, number_to)
        
        if predict_number == number:
            result = len(count)
            return result # завершение функции при угадывании числа
        elif predict_number > number:
            # сокращаем выборку, если предполагаемое число больше или меньше
            return count_number(number_from, predict_number + 1)
        else:
            return count_number(predict_number, number_to)
    
    result = count_number(number_from=1, number_to=101)
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