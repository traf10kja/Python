# hw_ex_1_less_2
num = input("Введите число: ")
sum = 0
for i in num:
   if i!=".":
       sum += int(i)
print(f'Сумма числа {num} составляет: ', sum)




#hw_ex_2_less_2
def factorial (number, count = 1):
   for i in range(1, number + 1):
       count *= i
   return count

n = int(input('Введите число: '))
for i in range(1, n + 1):
   print(f'{factorial(i)}', end = ', ')




# hw_ex_3_less_2
n = int(input('Введите число: ')) 
def sequence(n):
   return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   

print(sequence(n))
print(round(sum(sequence(n))))




# hw_ex_4_less_2
n = int(input("Введите число N: "))
lst_number = [i for i in range(-n, n+1)]
print(lst_number)

x = input("Укажите индексы чисел, через пробел, которые вы хотите перемножить: ").split()
print(x)
result = 1
for i in range(len(x)):
    x[i] = int(x[i])
    result *= lst_number[x[i]]  
print(result)




# hw_ex_5_less_2
import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Primary list: ")
print(list)
print("Mixed list: ")
print(mixed_list)