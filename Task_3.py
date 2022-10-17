# Задача 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением  дробной части элементов.
# Пример:
#        - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int (input('Введите значение длины списка n = '))
k = int (input('Введите значение количества знаков после запятой k = '))

Arr = []
for i in range(n):
     Arr.append(round(random.uniform(0, 10), k))
print(f'Сформированный список: {Arr}')

Arr2 = []
for i in range(n):
    fractional = round(Arr[i] % 1, k) # Убираем целую часть чисел
    Arr2.append(fractional)           # Формируем список из дробных частей
print(f'Список дробных частей: {Arr2}')
print(f'Максимальное значение дробной части = {max(Arr2)} минимальное значение = {min(Arr2)} ')
print(f'Разница максимального и минимального значения дробной части: {max(Arr2) - min(Arr2)}')