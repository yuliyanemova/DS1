"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    mn = 1
    mx = 101
    predict_number = np.random.randint(1, 101) # предполагаемое число
    
    while True:
        count += 1
        middle = round(mx + mn) / 2
        if number > middle:
            mn = middle
        else:
            mx = middle
        if number == middle:
            break # выход из цикла, если угадали  
        elif count > 20:
            break # выход при превышении количества попыток 
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел        
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
