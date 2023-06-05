'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

# import sys

# def DegreePositive(a,b,res) :
#     if b == 0 :
#         return res
#     res *= a
#     return DegreePositive(a, b-1, res)

# def DegreeNegative(a,b,res) :
#     if b == 0 :
#         return res
#     res *= a
#     return DegreeNegative(a, b+1, res)

# try :
#     a = int(input('Введите число А: '))
#     b = int(input('Введите число B: '))
# except ValueError :
#     print('Это не число/неверное значение')
#     sys.exit()

# if a == 0 and b < 0 :
#     print('Ноль может иметь только положительную степень!')
#     sys.exit()

# res = 1

# if b == 0 :
#     result = 1
# elif b > 0 :
#     result = DegreePositive(a,b, res)
# else :
#     result = 1/DegreeNegative(a,b,res)

# print(f'Число {a} в степени {b} равно {result}')

'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*
2 2
    4
'''

# import sys

# def SumPositive(a,b) :
#     if b == 0 :
#         return a
#     a+=1
#     return SumPositive(a, b-1)

# def SumNegative(a,b) :
#     if b == 0 :
#         return a
#     a-=1
#     return SumNegative(a, b+1)

# try :
#     a = int(input('Введите число А: '))
#     b = int(input('Введите число B: '))
# except ValueError :
#     print('Это не число/неверное значение')
#     sys.exit()

# if b >= 0 :
#     result = SumPositive(a,b)
# else :
#     result = SumNegative(a,b)

# print(f'Сумма чисел {a} и {b} равна {result}')