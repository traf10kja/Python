# hw_ex_1_less_4
import math

pi = math.pi
print('Pi = ', pi)

d = float(input('Введите точность округления '))
print(f'Accuracy = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))





# hw_ex_2_less_4
a = int(input('Введите число: '))
list =[]
for i in range(1,a+1):
    if(a%i==0):
      list.append(i)
print(f'{a} = {list}')




# hw_ex_3_less_4
import random

list = [random.randint(0,19) for i in range (20)]
print(list)
new_list =[]
[new_list.append(i) for i in list if i not in new_list ]
print(new_list)




# hw_ex_4_less_4
import random

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())
if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())
if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())
print(f'{first}{second}{third}')





# hw_ex_5_less_4
import random


# запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0,101)

# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    
# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file34_1.txt", create_str(koef1))
write_file("file34_2.txt", create_str(koef2))

# нахождение суммы многочлена
with open('file34_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file34_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file34_res.txt", create_str(lst_new))
with open('file34_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")