# Задача 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#           Пример:
#                  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#def fib_positiv(n):

list_fib_positiv = []
list_fib_negativ = []
k = int (input('Введите число k: '))

# Формируем часть списка слева от 0, включая 0.
f0 = 0
f1 = 1
f2 = -1
list_fib_negativ.append(f0)
list_fib_negativ.append(f1)
list_fib_negativ.append(f2)

for i in range(2, k):
    f1, f2 = f2, f1 - f2 
    list_fib_negativ.append(f2)
    list_fib_negativ2 = list_fib_negativ[ : : -1] # Перевернули список

# Формируем часть списка справа от 0
f1 = 1
f2 = 1
list_fib_positiv.append(f1)
list_fib_positiv.append(f2)

for i in range(2, k):
    f1, f2 = f2, f1 + f2 
    list_fib_positiv.append(f2)

# Объединяем списки
list_final = list_fib_negativ2 + list_fib_positiv
print(list_final)