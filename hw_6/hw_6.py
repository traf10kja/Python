## hw_ex_1_less_6 (## hw_ex_5_less_1)
#Семинар 1. Задание 5.
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# x1 = float(input('Введите х1: '))
# y1 = float(input('Введите y1: '))
# x2 = float(input('Введите х2: '))
# y2 = float(input('Введите y2: '))
# import math
# sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
# print(f'Расстояние от первой до второй точки составляет {sqrt}')



from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(f'Расстояние от первой до второй точки составляет {dot_range(dot_1, dot_2)}')



## hw_ex_2_less_6 (## hw_ex_2_less_2)
#Семинар 2. Задание 2.
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def factorial (number, count = 1):
#    for i in range(1, number + 1):
#        count *= i
#    return count

# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#    print(f'{factorial(i)}', end = ', ')


from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1),list(range(1, n + 1)))))

## hw_ex_3_less_6 (## hw_ex_1_less_3)
#Семинар 3. Задание 1. 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12


# list = [2, 3, 5, 9, 3, 5]
# print(list)
# sum = 0
# for i in range(len(list)):
#     if i %  2 != 0:
#         sum = sum + list[i]
# print(f'Сумма элементов на нечетных позициях {list} равна', sum)


my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(f'Сумма элементов на нечетных позициях {sum(my_list[1::2])} равна')



## hw_ex_4_less_6 (## hw_ex_2_less_3)
#Семинар 3. Задание 2.
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# list = [2,3,4,5,6]
# print(list,'=>', end=' ')
# def mult(list):
#     mult = []
#     for i in range((len(list)+1)//2):
#         mult.append(list[i]*list[len(list)-1-i])
#     return mult
# print(mult(list))


import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))