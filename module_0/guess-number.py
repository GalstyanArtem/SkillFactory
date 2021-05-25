import numpy as np

'Загадано число от 1 до 100, необходимо отгадать его за меньшее количество попыток'

number = np.random.randint(1, 101)         # загаданное число
print("Загадано число от 1 до 100")


def binary_search(number) :                # бинарная функция
    count = 0                              # счетчик попыток
    lower_bound = 0                        # нижняя граница
    upper_bound = 100                      # верхняя граница
    while lower_bound <= upper_bound:      # цикл
        middle = (lower_bound + upper_bound) // 2
        count += 1                         # плюсуем попытку
        if number == middle:
            return middle
        elif number > middle:
            upper_bound = middle - 1
        elif number < middle:
            lower_bound = middle + 1
    print(f"Вы угадали число {number} за {count} попыток.")


def score_game():
    """Запустите игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""

count_ls = []
np.random.seed(1)  # изменить случайную скорость
random_array = np.random.randint(1,101, size = (1000))

for number in random_array: # run binary_search on each of generated number
        count_ls.append(binary_search(number))
        score = np.mean(count_ls)     # запустите binary_search для каждого сгенерированного числа
 print(f" Algorithm guesses a number in  {score} attempts in average")

binary_search(number)
