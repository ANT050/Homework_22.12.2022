# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) и список коэффициентов  (-100..100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from random import randint
from sympy import symbols
from math import prod
from pathlib import Path

degree = int(input('\nВведите натуральную степень k:'))
x = symbols('x')

#Содание списков коэффициентов и степеней
list_coefficients = []
list_degrees = []

for i in range(degree+1):
    list_coefficients.append(random.randint(-100, 100))
    list_degrees.append(x**i)
list_degrees = list(reversed(list_degrees))

result = sum(map(prod, zip(list_coefficients, list_degrees)))

print(f'Список коэффициентов: {list_coefficients}')
print(f'\nМногочлен: {result} = 0')

#Создание файла с результатом в указнной папке
try:
  polynomial = Path.cwd()/'Task_1'/'result.txt'
  with open(polynomial, 'w', encoding='utf-8') as file:
    file.write(f'Натуральная степень k = {degree}')
    file.write(f'\nСписок коэффициентов: {list_coefficients}')
    file.write(f'\nМногочлен: {result} = 0')
except FileNotFoundError:
  print('\nФайл или директория не существует')
