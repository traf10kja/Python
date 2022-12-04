# hw_ex_1_less_3
list = [2, 3, 5, 9, 3, 5]
print(list)

sum = 0
for i in range(len(list)):
    if i %  2 != 0:
        sum = sum + list[i]
print(f'Сумма элементов на нечетных позициях {list} равна', sum)



# hw_ex_2_less_3
list = [2,3,4,5,6]
print(list,'=>', end=' ')

def mult(list):
    mult = []
    for i in range((len(list)+1)//2):
        mult.append(list[i]*list[len(list)-1-i])
    return mult
print(mult(list))



# hw_ex_3_less_3
lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst)

new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))



# hw_ex_4_less_3
a = int(input('Введите число: '))
b = ''
while a > 0:
    b = str(a % 2)+b
    a = a//2
print(b)



# hw_ex_5_less_3
a = int(input('Введите число: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')
