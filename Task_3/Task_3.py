# Написать свой рандомайзер (не использовать библиотеку RANDOM)

import time

minimum = int(input('\nВведите минимальное число диапазона: '))
maximum = int(input('Введите максимальное число диапазона: '))

def random_value(minimum, maximum):
    difference = maximum-minimum
    random = int(time.time()*10000000)
    random %= difference
    random += minimum
    return random

print(f'\nРандомное значение диапазона ({minimum}-{maximum}): {random_value(minimum, maximum)}')