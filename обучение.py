
# a = int (input())
# b = int (input())
# if a >= b :
#     print (b)
# else:
#    print (a) 



    
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())   
# if  a<b:
#     x = a
# else:
#     x = b
# if c<d:
#     y = c
# else:
#     y = d
# if x<y :
#     print(x)
# else: 
#     print (y)


# a = int(input())
# b = int(input())
# c = int(input())
# if 0 <= a :
#     x = a
# else:
#     x = 0 
# if 0 <= b :
#     y = b
# else:
#     y = 0
# if 0 <= c :
#     z = c
# else:
#     z = 0
# print(x+y+z)



# a = int(input())
# if -1 < a < 17 :
#     print("Принадлежит")
# else:
#     print("Не Принадлежит")

# if a + b == c and a + c == b and b + c == a: # проверка на треугольник
# 4.3.3.
# a,b,c = int(input()),int(input()),int(input())  
# if a + b == c and a + c == b and b + c == a: # проверка на треугольник
#     if a == b == c:
#          print("Равностороний")
#     elif a == b or a == c or b == c:
#         print("Равнобедренный")
#     else:
#         print("Разностороний")
# else:
#     print()
#ФРИК ЕБАНЫЙ НЕ РАБОТАЕТ 4.3.3
 
# a,b = input(),input()
# if a == "красный" and b == "синий" or a == "синий" and b == "красный":
#     print("фиолетовый")
# elif a == "красный" and b == "желтый" or a == "желтый" and b == "красный":
#     print("оранжевый")
# elif a == "синий" and b == "желтый" or a == "желтый" and b == "синий":
#     print("зеленый")
# elif a == "красный" and b == "красный" or a == "красный" and b == "красный":
#     print("красный")
# elif a == "синий" and b == "синий" or a == "синий" and b == "синий":
#     print("синий")
# elif a == "желтый" and b == "желтый" or a == "желтый" and b == "желтый":
#     print("желтый")
# else:
#       print("ошибка цвета")

# a = int(input())
# if 0 <= a <= 36:
#     if a == 0:
#         print("зеленый")
#     if 1 <= a <= 10:
#         if a % 2 != 0:
#             print("красный")
#         else:
#             print("черный")
#     if 11 <= a <= 18:
#         if a % 2 != 0:
#             print("черный")
#         else:
#             print("красный")
#     if 19 <= a <= 28:
#         if a % 2 != 0:
#             print("красный")
#         else:
#             print("черный")
#     if 29 <= a <= 36:
#         if a  % 2 != 0:
#             print("черный")
#         else:
#             print("красный")
# else: 
#     print("ошибка ввода")

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# # Проверяем, есть ли пересечение
# if b1 < a2 or b2 < a1:  # Если один отрезок полностью левее или правее другого
#     print("пустое множество")
# else:
#     # Находим границы пересечения вручную
#     if a1 >= a2:
#         start = a1
#     else:
#         start = a2

#     if b1 <= b2:
#         end = b1
#     else:
#         end = b2

#     # Проверяем тип пересечения
#     if start == end:  # Точка
#         print(start)
#     else:  # Отрезок
#         print(start, end)
        

# if a + b == ["Желтый"]:
#     print("Желтый")
# if a + b == "Красный":
#     print("Красный")
# elif a + b == "Синий":
#     print("Синий")
# if a == "Желтый":
#     b == "Красный"
#     a + b == "Оранжевый"
#     print("Оранжевый")
# elif a == "Желтый":
#     b == "Синий"
#     print("Зелeный")
# elif a == "Красный":
#     b == "Синий"
#     print("Фиолетовый")

# a = int(input())
# if 1 <= a <= 10:
#     if a == 1:
#         print("I")
#     if a == 2:
#         print("II")
#     if a == 3:
#         print("III")
#     if a == 4:
#         print("IV")
#     if a == 5:
#         print("V")
#     if a == 6:
#         print("VI")
#     if a == 7:
#         print("VII")
#     if a == 8:
#         print("VIII")
#     if a == 9:
#         print("IX")
#     if a == 10:
#         print("X")
# else:
#     print("ошибка")

# a = int(input())
# if a % 2 == 0:
#     if 2 <= a <= 5:
#         print("NO")
#     if 6 <= a <= 20:
#         print("YES")
#     if 21 <= a:
#         print("NO")
# else:
#     print("YES")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 - y2  == x2 - y1 or x1 + y2 == x2 + y1:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print("YES")
#     if x1 != x2:
#         print("YES")
#     if y1 != y2:
#         print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1==x2 and y1!=y2) or (x1 != x2 and y1 == y2) or (x1 - x2) == (y1 - y2):
#     print("YES")
# else:
#     print("NO")


# v1 = float(input())
# v2 = float(input())
# s  = float(input())
# print (s / (v1 + v2)) 

# a = float(input())
# if a == 0:
#     print("Обратного числа не существует")
# else:
#     print(1 / a)

# a = float(input())
# print(5 / 9 * (a - 32))


# a = float(input())
# if a <= 2:
#     print(a * 10.5)
# else:
#     print(21 + (a - 2) * 4)

# a = float(input())
# zxc = int((a * 10) % 10)
# print(zxc)


# a = float(input())
# print(float(a)- int(a))


# a, b, c = int(input()), int(input()), int(input())
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b < c:
#     b, c = c, b
# print(a)
# print(b)
# print(c)

# num = int(input())
# hundreds = num // 100  # Сотни
# tens = (num // 10) % 10  # Десятки
# ones = num % 10  # Единицы
# max_digit = max(hundreds, tens, ones)  
# min_digit = min(hundreds, tens, ones)
# if hundreds != max_digit and hundreds != min_digit:
#     middle_digit = hundreds
# elif tens != max_digit and tens != min_digit:
#     middle_digit = tens
# else:
#     middle_digit = ones
# if max_digit - min_digit != middle_digit:
#     print("Число неинтересное")
# else:
#     print("Число интересное")


# a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
# sum_digit = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
# print(sum_digit)

# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# num = abs(p1 - q1) + abs(p2 - q2)
# print(num)

# proposal = '"Python is a great language!", said Fred. ' + '"I don\'t ever remember having this much fun before."'
# print(proposal)

# name = input()
# surname = input()
# z = " "
# print("Hello" + z + name + z + surname + "!" + z + "You have just delved into Python")


# club = input()
# length1 = len(club)
# print("Футбольная команда " + club + " имеет длину " + str(length1) + " символов")


# town1, town2, town3 = input(), input(), input()
# lenght1, lenght2, lenght3 = len(town1), len(town2), len(town3)
# min_town = min(town1, town2, town3, key=len)
# max_town = max(town1, town2, town3, key=len)
# print(min_town)
# print(max_town)

# a = len(input())
# b = len(input())
# c = len(input())
# if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
#     print("YES")
# else:
#     print("NO")

# a = input()
# if "синий" in a:
#     print("YES")
# else:
#     print("NO")

# a = input()
# if "суббота" in a:
#     print("YES")
# elif "воскресенье" in a:
#     print("YES")
# else:
#     print("NO")
    

# a = input()
# if "суббота" in a or "воскресенье" in a:
#     print("YES")
# else:
#     print("NO")


# adres = input()
# if "@" in adres and "." in adres:
#     print("YES")
# else:
#     print("NO")


# Функция	Описание
#                                                     Округления
# int()	Округляет число в сторону нуля
# round(x)	Округляет число x до ближайшего целого. Если дробная часть числа равна 
# 0.5
# 0.5, то число округляется до ближайшего четного числа (банковское округление)
# round(x, n)	Округляет число x до n знаков после точки
# floor(x)	Округляет число x вниз («пол»)
# ceil(x)	Округляет число x вверх («потолок»)
# abs(x)	Модуль числа x (абсолютная величина)
#                                             Корни, логарифмы, степени и факториал
# sqrt(x)	Квадратный корень числа x
# pow(x, n)	Возведение числа x в степень n
# log(x)	Натуральный логарифм числа x. Основание натурального логарифма равно числу e
# log10(x)	Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
# log(x, b)	Логарифм числа x по основанию b
# factorial(n)	Факториал натурального числа n
#                                                 Тригонометрия
# degrees(x)	Преобразует угол x, заданный в радианах, в градусы
# radians(x)	Преобразует угол x, заданный в градусах, в радианы
# cos(x)	Косинус угла x, задаваемого в радианах
# sin(x)	Синус угла x, задаваемого в радианах
# tan(x)	Тангенс угла x, задаваемого в радианах
# acos(x)	Возвращает угол в радианах от 0 до π, cos которого равен x
# asin(x)	Возвращает угол в радианах от −π/2 до 2/π​, sin которого равен x
# atan(x)	Возвращает угол в радианах от −π/2 до 2/π  , tan которого равен x
# atan2(y, x)	Полярный угол (в радианах) точки с координатами (x, y)
# Для извлечения квадратного корня можно воспользоваться кодом n ** 0.5, вместо math.sqrt(n).

#                                         Список констант модуля math
# Модуль math предоставляет ряд встроенных математических констант:

# Константа   pi    Число π = 3.141592653589793
# Константа   e    Число e = 2.718281828459045 (константа Эйлера)

# Примечание 1. Все функции модуля math возвращают значение, которое можно вывести на экран, присвоить другой переменной или использовать в математическом выражении.
# Примечание 2. Для использования функций int(), float(), abs(), min(), max(), round() подключать модуль math нет необходимости. Это так называемые встроенные функции.
# Примечание 3. Вызов функций pow(x, n) можно заменить использованием оператора возведения в степень: x**n.
# Примечание 4. Импортировать функции (или любые другие объекты) из модуля можно несколькими способами:
    
    
#     from math import *

# num = sqrt(10)
# from math import sqrt

# num = sqrt(10)
# import math

# num = math.sqrt(10)


# Однако рекомендуется избегать импортирования через from math import *, так как нет ясности, 
# какие функции были импортированы и это загрязняет пространство имён лишними, неиспользуемыми функциями. 
# Вместо этого рекомендуется использовать from math import sqrt или import math, чтобы явно указать,
# что именно вы импортируете. Это делает ваш код более читаемым и управляемым.



# from math import *
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# num1 = sqrt((x1 - x2)**2 +(y1 - y2)**2)
# print(num1)

# from math import *
# r = float(input())
# s = pi * r**2
# c = 2 * pi * r
# print(s)
# print(c)

# from math import *
# a = float(input())
# b = float(input())
# print((a+b)/2)
# print(sqrt(a*b))
# print((2*a*b)/(a+b))
# print(sqrt((a**2 + b**2) / 2))

# from math import *
# x = float(input())
# r = x * pi / 180
# num = (sin(r) + cos(r) + tan(r)**2)
# print(num)


# from math import *
# x = float(input())
# num = floor(x) + ceil(x)
# print(num)

    
# from math import sqrt

# a = float(input())
# b = float(input())
# c = float(input())

# d = b**2 - 4 * a * c  # вычисление дискриминанта

# if d > 0:
#     # Вычисляем два корня по формуле:
#     x1 = (-b - sqrt(d)) / (2 * a)
#     x2 = (-b + sqrt(d)) / (2 * a)
#     # Выводим корни в порядке убывания (больший корень первым)
#     if x1 < x2:
#         print(x1)
#         print(x2)
#     else:
#         print(x2)
#         print(x1)
# elif d == 0:
#     # Один корень
#     x = -b / (2 * a)
#     print(x)
# else:
#     # Если дискриминант отрицательный, корней нет
#     print("Нет корней")


# from math import *

# n = int(input())
# a = float(input())

# s = (n * a**2) / (4 * tan(pi / n))
# print(s)

# for i in range(10):
#     print("Python is awesome!")

# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")


# a = input()
# b = int(input())
# for i in range(b):
#     print(a)
    
    
# a = ("*"*19)
# b = int(input())
# for i in range(b):
#     print(a)



# a = input()
# for i in range(10):
#     print(i,a)


# i = int(input())
# for i in range(i+1):
#     print("Квадрат числа", i, "равен", i*i)


# a = "*"
# b = int(input())
# for i in range(b, 0, -1):
#     print(a*i)


# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     print(i+1 ,m * (p / 100 + 1) ** i)

# m = int(input())
# n = int(input())
# for i in range(m,n+1):
#     print(i)


# m = int(input())
# n = int(input())
# if m>n:
#     for i in range(m+1,n,-1):
#         print(i-1)
# else:
#     for i in range(m,n+1,1):
#         print(i)


# m = int(input())
# n = int(input())
# a = ((m - 1) // 2) * 2 + 1
# for i in range(a, n -1, -2 ):
#     print(i)
    

# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif i % 17 == 0:
#         print(i)

# n = int(input())
# a = "x"
# for i in range(1,11):
#     print(n,a,i,"=",n*i)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)


# a = int(input())
# b = int(input())
# counter = 0
# for i in range(a,b+1):
#     if (i**3 % 10 == 4) or (i**3 % 10 == 9):
#         counter = counter + 1
# print(counter)


# n = int(input())
# totalsum = 0
# for _ in range(n):
#     number = int(input())
#     totalsum += number
# print(totalsum)

# from math import *
# n = int(input())
# a = 0
# start = 1
# end = 1 / n
# step = 1 / n
# for i in range(1, n + 1):
#     a += 1 / i
# print(a - log(n))


# n = int(input())
# sum1 = 0 
# for i in range(1, n+1):
#     if i**2 % 10 == 2:
#         sum1 +=  i 
#     elif i**2 % 10 ==  5:
#         sum1 +=  i
#     elif i**2 % 10 == 8:
#         sum1 +=  i 
# print(sum1)


# n = int(input())
# a = 1
# for i in range(1, n+1):
#     a = i * a
# print(a)


# a = 1
# for i in range(10):
#     n = int(input()) 
#     if n != 0:
#         a *= n
# print(a)

# n = int(input())
# a = n
# sum1 = 0
# for i in range(1, a+1):
#     if n % i == 0:
#         sum1 += i
# print(sum1)


# n = int(input())
# sum1 = 0

# for i in range(1, n + 1):  # Перебираем числа от 1 до n
#     if n % i == 0:         # Проверяем, является ли i делителем n
#         sum1 += i         # Суммируем делитель i

# print(sum1)


# n = int(input())
# sum1 = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum1 += i
#     else:
#         sum1 -= i
# print(-sum1)

# n = int(input())
# max1 = -1
# min1 = -1
# for i in range(n):
#     n = int(input())
#     if max1 < n:
#         min1 = max1
#         max1 = n
#     elif n > min1:
#         min1 = n
# print(max1, min1, sep="\n")



# a = True
# for i in range(1,11):
#     num = int(input())
#     if num % 2 == 0:
#         a = True
#         print("YES")
#     else:
#         print("NO")

# num = 0
# for i in range(1,11):
#     firs_digit = int(input())
#     if firs_digit % 2 == 0:
#         num += 1
# if num == 10:
#     print("YES")
# else:
#     print("NO")


# a = 1  # Первое число Фибоначчи
# b = 1  # Второе число Фибоначчи
# n = int(input())  # Ввод количества чисел
# if n == 1:
#     print(1)  # Выводим 1 при n = 1
# else:
#     print(a, end=" ")  # Выводим первое число
#     for _ in range(1, n):
#         a, b = b, a + b
#         print(a, end=" ")


# text = input()
# while text != "КОНЕЦ":
#     print(text)
#     text = input()
    
    
# text = input()  # Чтение первой строки
# while text != "КОНЕЦ" and text != "конец":  # Проверка на оба варианта
#     print(text)  # Вывод текущего слова
#     text = input()  # Чтение следующей строки


# text = input()  # Чтение первой строки
# count = 0  # Счётчик слов

# while text != "стоп" and text != "хватит" and text != "достаточно":  # Проверка на стоп-слова
#     count += 1  # Увеличиваем счётчик
#     text = input()  # Чтение следующей строки

# print(count)  # Вывод количества слов

# flag = True
# num = int(input())
# while num % 7 == 0 or num == 0:
#         print(num)
#         num = int(input())


# digit = int(input())
# sum1 = 0
# while digit >= 0:
#         sum1 += digit 
#         digit = int(input())
# print(sum1) 

# five = 0
# num = int(input())
# while 5 >= num > 0:
#         if num == 5:
#                 five += 1
#                 num = int(input())
#         else:
#                 num = int(input())
# print(five)



# money = int(input())
# counter = 0


# while money >= 25:
#         counter += 1
#         money -= 25
# while money >= 10:
#         counter += 1
#         money -= 10
# while money >= 5:
#         counter += 1
#         money -= 5
# while money >= 1:
#         counter += 1
#         money -= 1
        
        
# print(counter)


# num = int(input())
# last_digit = 0
# while num > 0:
#         last_digit = num % 10
#         num = num // 10
#         print(last_digit)

# num = int(input())
# digit = 0
# while num > 0:
#         digit = num % 10
#         num = num // 10
#         print(digit, end="")

# num = int(input())
# max_digit = 1
# min_digit = 9
# digit = 0
# while num > 0:
#         digit = num % 10
#         num = num // 10
#         if max_digit < digit:
#                 max_digit = digit
#         if min_digit > digit:
#                 min_digit = digit
# print("Максимальная цифра равна",max_digit)
# print("Минимальная цифра равна", min_digit)

# sum_num = 0
# digit = 0
# counter = 0
# average = 1
# first_digit = 0
# fs_digit = 0
# num = int(input())
# while num > 0:
#         sum_num += num % 10
#         counter += 1
#         digit *= sum_num 
#         num = num // 10
# print(sum_num)
# while num > 0:
#         digit = num % 10
#         digit *= digit
#         num = num // 10
# print(digit)
        
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)
# for i in range(10):


# n = int(input())
# for i in range(2, n+1):
#     if n % i == 0:
#         print(i)
#         break


# n = int(input())
# for i in range(1, n+1):
#     if 4 < i < 10 or 16 < i < 38 or 77 < i < 88:
#         continue
#     print(i)


# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print("NO")


# max1 = None
# sum1 = 0 # сумма отриц чисел
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         if max1 is None or x > max1:
#             max1 = x
#         sum1 += x
# if max1 is None:
#     print("NO")
# else:
#     print(sum1)
#     print(max1)



# s = 0
# for _ in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)


# n = int(input())
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# a = 0
# while n > 0:
#     a = n % 10
#     n = n // 10
# print(a)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)


# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)


# n = int(input())
# for i in range(n):
#     for i in range(3):
#         print(n, end=" ")
#     print()


# n = int(input())
# for i in range(1, n+1):
#     for j in range(5):
#         print(i, end=" ")
#     print()



# n = int(input())
# for i in range(1, n + 1):
#     for k in range (1, 10):
#         print(i, "+", k, "=", i + k)
#     print()
    
    
# n = int(input("Введите число: "))

# for i in range(1, n + 1):  # Внешний цикл от 1 до n
#     for k in range(1, 10):  # Внутренний цикл от 1 до 9
#         print(i, "+", k, "=", i + k)
#     print()  # Пустая строка после каждого блока


# n = int(input())

# # Верхняя часть (увеличение)
# for i in range(1, n // 2 + 2):  # До середины включительно
#     print("*" * i)

# # Нижняя часть (уменьшение)
# for i in range(n // 2, 0, -1):  # От середины-1 до 1
#     print("*" * i)


# n = int(input())
# for i in range(1, n + 1):
#     print('*' * min(i, n - i + 1))


# n = int(input())
# for i in range(1, n + 1):
#     for k in range(i):
#         print(i, end = "")
#     print()


# total = 0
# for n in range(1, 28):
#     for k in range(1, 30):
#         for m in range(1, 31):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)  

# a = 10
# b = 5
# c = 0.5

# # Перебираем count1 и count2, а count3 вычисляем из условия
# for count1 in range(1, 100):
#     for count2 in range(1, 100):
#         # Вычисляем count3 из условия count1 + count2 + count3 == 100
#         count3 = 100 - count1 - count2
#         if count3 > 0:  # Проверяем, что count3 положительное
#             # Проверяем второе условие
#             if count1 * a + count2 * b + count3 * c == 100:
#                 print(count1, count2, count3)


# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 # Вычисляем e как корень пятой степени из суммы a^5 + b^5 + c^5 + d^5
#                 total = a**5 + b**5 + c**5 + d**5
#                 e = round(total ** (1/5))
#                 # Проверяем, выполняется ли условие
#                 if e**5 == total and e <= 150:
#                     print(f"Найдено решение: {a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")
#                     exit()  # Завершаем программу после нахождения решения


# a = 0
# n = int(input())
# for i in range(n+1):
#     for k in range(i):
#         a += 1
#         print(a, end = " ")
#     print()


# n = int(input())
# for i in range(1, n+1):
#     for k in range(1, i + 1):
#         print(k, end = "")
#     for j in range(i - 1, 0, -1):
#         print(j, end = "")
#     print()


# a = int(input())
# b = int(input())

# max_total = 0  # Максимальная сумма делителей
# best_number = a  # Число с максимальной суммой делителей

# for i in range(a, b + 1):
#     total = 0  # Сумма делителей текущего числа
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total += j
#     # Если текущая сумма делителей больше или равна максимальной, обновляем значения
#     if total > max_total or (total == max_total and i > best_number):
#         max_total = total
#         best_number = i

# # Вывод результата
# print(best_number, max_total)



# plus = "+"
# digit = 0
# count = 0
# n = int(input())

# for i in range(1, n + 1):
#     count = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             count += 1
#             digit = count * plus

#     print(i, digit, sep = "")


# num = int(input())  # Вводим число с клавиатуры и преобразуем его в целое число
# while num > 9:  # Пока число больше 9 (т.е. пока оно не однозначное)
#     sum1 = 0  # Инициализируем переменную для хранения суммы цифр
#     while num > 0:  # Пока число больше 0
#         last_digit = num % 10  # Получаем последнюю цифру числа
#         sum1 += last_digit  # Добавляем последнюю цифру к сумме
#         num = num // 10  # Убираем последнюю цифру из числа
#     num = sum1  # Присваиваем num значение суммы цифр
# print(num)  # Выводим итоговое однозначное число


# from math import *
# n = int(input())
# sum1 = 0
# for i in range(1, n + 1):
#     sum1 += factorial(i)
# print(sum1)


# a, b = int(input()), int(input())  # Вводим диапазон [a, b]

# for k in range(a, b + 1):  # Перебираем все числа от a до b
#     if k < 2:  # Числа меньше 2 не являются простыми
#         continue
#     is_prime = True  # Предполагаем, что число простое
#     for i in range(2, int(k**0.5) + 1):  # Проверяем делители от 2 до корня из k
#         if k % i == 0:  # Если делится без остатка
#             is_prime = False  # Число не простое
#             break  # Выходим из цикла
#     if is_prime:  # Если число простое
#         print(k)  # Выводим его


# a = input()
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i])
#     else:
#         continue

# s = input()
# for i in range(len(s) -1, - 1, - 1):
#     print(s[i])

# name = input()
# surname = input()
# patronymic = input()
# print(surname[0], name[0], patronymic[0], sep = "")


# sum1 = 0
# s = input()
# for i in range(0, len(s), 1):
#     sum1 += int(s[i])
# print(sum1)


# s = input()
# digits = '0123456789'

# for c in s:
#     if c in digits:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# s = input()
# plus = 0
# count = 0

# for char in s:  # Перебираем каждый символ строки
#     if char == "+":
#         plus += 1
#     if char == "*":
#         count += 1

# print("Символ", '+', "встречается", plus, "раз")
# print("Символ", '*', "встречается", count, "раз")

