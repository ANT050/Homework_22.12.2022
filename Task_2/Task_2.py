#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.

from pathlib import Path

try:
  first_file = open('Task_2/file_1.txt', 'r')
  file_1 = first_file.readline()
  
  second_file = open('Task_2/file_2.txt', 'r')
  file_2 = second_file.readline()
  print(f'\n({file_1}) + ({file_2})')
  
  outpath_sum = Path.cwd()/'Task_2'/'sum_poly.txt'
  with open(outpath_sum, 'w', encoding='utf-8') as file:
    file.write(f'({file_1}) + ({file_2})')

except FileNotFoundError:
  print('Файл или директория не существует')