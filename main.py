#подсчет букв и текста большие маленькие
# name = input("Enter your name: ")
#
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(f'{len(name)} букв' )


#подсчет возраста больше меньше
# age = int(input('твой возраст какой? '))
#
# if age < 20:
#     print('твой возраст меньше 20')
#
# elif age > 20:
#     print('твой возраст больше 20')
#
# elif age == 20:
#     print('твой возраст 20')




# name = input('страна? ').lower()
#
# if name == 'кыргызстан':
#     print(f'{name} салам')
#
# elif name == 'россия':
#     print(f'{name} привет')
#
# elif name == 'китай':
#     print(f'{name} нихаома')



# name = int(input('Какую оценку получил:? '))
#
# if name == 5:
#     print('Отлично')
#
# elif name == 4:
#     print('Хорошо')
#
# elif name == 3:
#     print('Удовлетворительно')
# ')
# elif name == 2:
#     print('плохо')



# name = input('что говорит животное: ')
#
# if name == 'собака':
#     print('гав гав')
#
# elif name == 'кошка':
#     print('мяу мяу')
#
# elif name == 'корова':
#     print('му му')



# price = int(input('Введите сумму покупки: '))
#
# if price >= 5000:
#     discound = 20
# elif price >= 2000:
#     discound = 10
# elif price >= 1000:
#     discound = 0
#
# skidka = price * discound / 100
# final = price - skidka
#
# print(f'Ваша скидка состовляет {discound}% ')
# print(f'Итого к оплате {final} сом ')




# age = int(input('Можно узнать ваш возраст?: '))
#
# if age <= 12:
#     price = 150
#
# elif age <= 18:
#     price = 250
#
# elif age <= 30:
#     price = 350
# else:
#     price = 400
#
# print(f'Цена вашего билета {price} сом')



# km = int(input('Сколько км до вашего дома от нашей точки?: '))
#
# if km <= 5:
#     price = 150
# elif km <= 10:
#     price = 250
# elif km <= 15:
#     price = 400
# else:
#     price = 500
#
# print(f'Цена доставки составит {price} сом')



# time = int(input('На сколько минут собираетесь арендовать самокат?: '))
#
# if time <= 10:
#     price = 80
# elif time <= 30:
#     price = 200
# elif time <= 60:
#     price = 500
# else:
#     price = 1000
#
# print(f'Стоимость аренды самоката состовляет {price} сом')



# age = int(input('Для продажи табака нужно не менее 18 лет. Сколько вам лет? : '))
# passport = int(input('Есть паспорт у вас? (1 - да, 0 - нет): '))
#
# if age >= 18 and passport == 1:
#     print('Продажа разрешена')
# else:
#     print('Продажа запрещена')



# age = int(input('Сколько вам лет?: '))
# code = int(input('Вы соблюдаете дресс код ночного клуба? (1 - да, 0 - нет): '))
#
# if age >= 21 and code == 1:
#     print('Добро пожаловать в клуб')
# else:
#     print('Вам вход запрещен')




# age = int(input('Сколько вам лет? для одобрения кредита нужно не менее 21: '))
# income = int(input('Ваш доход сколько состовляет?: '))
# sum = int(input('Какую сумму хотите в кредит взять?: '))
#
# if age >= 21 and income >= 40000:
#     print('Вам одобрили кредит')
# else:
#     print('Вам отказали брать кредит')


# student = int(input('Для студентов есть скидки в магазине, ты студент? (1 - да, 0 - нет) '))
# card = int(input('И для тех у кого есть дисконтная карта, у тебя есть дисконтная карта? (1 - да, 0 - нет) '))
# if student == 1 or card == 1:
#     print('Вам положена скидка в размере 10% от суммы ')
# else:
#     print('Вам не положена скидка')




# age = int(input('Для входа в закрытый клуб нужно не менее 18 лет, Сколько тебе лет?: '))
# black_list = int(input('И чтоб не был в черном списке! Ты есть в черном списке? (1 - да, 0 - нет): '))
#
# if age >= 18 and not black_list == 1:
#     print('Вам можно в клуб, проходите')
# else:
#     print('Вам нельзя в клуб')



# motion = int(input('Видишь подозрительное движение в магазине? (1 - да, 0 - нет): '))
# security = int(input('Включен режим охраны? (1 - да, 0 - нет): '))
#
# if motion == 1 and not security == 1:
#     print('тревога кража')
# else:
#     print('все спокойно')



# laptops = ['acer', 'macbook', 'lenovo', 'samsung']
#
# name = input('Какой модели у тебя ноутбук?: ')
# laptops.append(name)


# num1 = [2, 5, 8, 9]
# num2 = [12, 34, 56, 78]
# print(num1 + num2)
# or
# a = num1 + num2
# print(a)
# or
# num1.extend(num2)



# fruits1 = ['limon', 'apple', 'peach', 'apricot']
# fruits2 = ['cherry', 'pineapple', 'mango', 'watermelon']
#
# a = fruits1 + fruits2
# a.sort()
# print(a)


# cars = ['mers', 'bmw', 'porch', 'matiz']
#
# car = input('Машинанын атын жаз: ')
# if car in cars:
#     ca = cars.index(car)
#     print(f'индекс {ca}')


# phones = ['Iphone', 'Samsung', 'Xiaomi', 'Redmi', 'Poco', 'tesla']
# comp = ['Lenovo', 'Asus', 'Acer', 'Macbook', 'Xiaomi']
# a = phones + comp
# a.sort()
# print(a)
#
# indexed = input('Индекс какого устройства вы хоите узнать?: ')
# if indexed in a:
#     b = a.index(indexed)
#     print(f'Индекс данного устройства {b}')
#
# a = phones + comp
# a.sort()


# cars = ['merc', 'bmw', 'porch', 'matiz', 'merc', 'bmw', 'merc', 'porch']
# a = input('Название автомоиля?: ')
#
# count = cars.count(a)
# print(f'Количество {a}: {count} ')



# city = ['Bishkek', 'Osh', 'Naryn', 'Moscow',
# 'Astana', 'Almaty', 'Belgorod', 'Moscow', 'Bishkek', 'Bishkek', "Osh", "Osh", 'Moscow']
# n = input("Город?: ")
# count = city.count(n)
# print(f'Этот город упоминается здесь: {n}: {count}')



# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1',
#            '1', '1', '1', '1', '2', '2', '2', '6', '6', '6']
#
# n = input('Число?: ')
# count = numbers.count(n)
# print(f'Это число повторяется здесь {count} раз')


# laptops = ['hp', 'lenovo', 'acer', 'macbook',]
# laptop = input('название ноутбука: ')
# if laptop in laptops:
#     laptops.remove(laptop)
#     print(laptops)
# else:
#     print('у нас нету такого')


# comp = ['hp', 'lenovo', 'acer', 'asus',]



# car1 = ['mers', 'bmw', 'honda', 'audi']
# car2 = ['mers', 'tesla', 'bmw', 'ferari']
#
# car1.extend(car2)
# uni = set(car1)
# print(tuple(sorted(uni)))


# s = input('напиши слово : ').lower()
#
# if s == s [::-1]:
#     print('Палиндром')
#
# else:
#     print('не палиндром')




# laptops = ['lenovo', 'asus', 'macbook', 'dell']
# computer = ('acer', 'gigabyte', 'lenovo', 'dell')
#
# dd = set(laptops).intersection(computer)
# print(tuple(dd))

#('lenovo', 'dell')

# laptops = ['lenovo', 'asus', 'macbook', 'dell']
# computer = ('acer', 'gigabyte', 'lenovo', 'dell')
#
# dd = set(laptops).symmetric_difference(computer)
# print(tuple(dd))

#('gigabyte', 'asus', 'acer', 'macbook')


# считает уникальных
# colors = ['red', 'blue', 'red', 'black', 'green', 'blue']
#
# uni = set(colors)
# print(list (uni))
# print(len(uni))



# allowed_users = {'admin', 'guest', 'nursultan'}
#
# ss = input('Введите имя пользователя?: ').lower()
#
# if ss in allowed_users:
#     print('Доступ разрешен')
# else:
#     print('Пользователь не найден ')





# na = {'quen', 'karol'}
# name = (input('кто вы?: ')).lower()
#
# if name in na:
#     print('Вход выполнен ')
# else:
#     print('Вход запрещен ')



#
# Python
# 1. Типы Данных 8
# 1.1. Измен 3
# list [], [4, 345] append, extend, index, clear, pop,
# remove, count, insert, sort, reverse,
# set set(), {1, 3, 5, 2} (difference(), symmetric_difference(), intersection(),
#                          onion, add, remove, discard)
# dict {},
# person = {'name': 'Asan',
#           'city': 'Bishkek',
#           'subject': 'Math',
#           'job': 'IT'}
# subj = person['subject'] = 'History'
# del person['city']
# print(person.pop("path", "Backend")  )
# cl = person.clear()
# print(cl)

# 1.2. Неизмен 5
# int
# float /, //, %, **
# bool >, <, ==, !=, >=, <=
# str "asdf", "2345" lower, upper, title, capitalize, len, split, join
# tuple (), (5, 45) count, index,




# Цикл
# for name in range(10):
#     print('Hello World')

# for name in range(1, 11, 2):
#     print(name)

# fruits = ["яблоко", "банан", "вишня", 'дыня']
# for fruit in fruits:
#     print(fruit)


# person = {"имя": "Иван", "возраст": 25, "город": "Москва"}
# for key in person:
#     print(key, ":", person[key])




# cars = ['bmw', 'mers', 'porch', 'toyota', 'tesla']
#
# for ss in cars:
#     print(ss)

# сортирует по алфавиту
# cars = ['bmw', 'mers', 'porch', 'toyota', 'tesla', 'audi']
#
# for ss in sorted(cars):
#     print(ss)


# с индексом выводит
# cars = ['bmw', 'mers', 'porch', 'toyota', 'tesla', 'audi']
#
# for i in enumerate(cars):
#     print(i)


# пурувернуть
# numbers = (5, 8, 3, 1, 9, 4)
# for number in reversed(numbers):
#     print(number)

# numbers = (5, 8, 3, 1, 9, 4)
# for name in numbers[::-1]:
#     print(name)



# laptops = ('Acer', 'GiGABYTe', 'lEnOVO', 'MacBOOk')
#
# for name in reversed(laptops):
#     print(name.title())

# отрицательные выводить
# numbers = [2, -4, 6 -8, -1, 5]
# for name in numbers:
#     if name < 0:
#         print(name)


# добавляет в лист
# numbers = [2, -4, 6, -8, -1, 5]
# list = []
# for name in numbers:
#     if name > 0:
#      list.append(name)
# print(list)



# сортирует и в тапл превращает
# my_laptops = ['Acer', 'LenoVo', 'HP', 'AsuS']
# new_list = []
# for lap in sorted(my_laptops):
#     new_list.append(lap.title())
#
# print(tuple(new_list))




# Количесво цифр = Количество строк со словом
# a = int(input('сан  жаз: '))
# b = input('соз жаз: ')
#
# for с in range(a):
#     print(b)




# numbers = [9, -7, 3, -2, -7, 2]
# new_list = []
# for name in numbers:
#     if name < 0:
#         new_list.append(0)
#     else:
#         new_list.append(name)
#     print(tuple(new_list))


# добавление нового листа и замена данных внутри листа
# numbers = [9, -7, 3, -2, -7, 2]
# new_my_list = []
# for i in numbers:
#     if i < 0:
#         new_my_list.append(0)
#     else:
#         new_my_list.append(i)
# print(tuple(new_my_list))



# четные числа, деление цифр остатков
# a = int(input('Введите цифру: '))
#
# if a % 2 == 0:
#     print('Четное')
# else:
#     print('нечетное')



# определение разделением четное нечетное
# numbers = [2, 4, 7, 9, 5, 6]
# newl = []
# newll = []
# for num in numbers:
#     if num % 2 == 0:
#         newl.append(num)
#     else:
#         newll.append(num)
#
#     print(f'четное: {newl}')
#     print(f'нечетное: {newll}')

# numbers = [2, 4, 7, 9, 5, 6]
# jup_san = []
# tak_san = []
# for i in numbers:
#     if i % 2 == 0:
#         jup_san.append(i)
#     else:
#         tak_san.append(i)
#
# print(f'четные : {jup_san}')
# print(f'Нечетные : {tak_san}')



# лист палиндром не палиндром
# ddd = ('kazak', 'python', 'car', 'wallet', 'madam')
# newl = []
# newll = []
# for name in ddd:
#     if name == name[::-1]:
#         newl.append(name)
#     else:
#         newll.append(name)
#     print(f'палиндром {name} ')
#     print(f' не палиндром {name} ')




# n = input('соз жаз?: ')
# while True:
#     print(n)
#     if input('стоп'):
#         break


# бесконечность цикла
# num = 0
# while True:
#     num += 1
#     print(num)




#Бескочный сбор данных до момента стоп
# while True:
#     word = input('Соз жаз: ')
#     if word == 'stop':
#         break




# count = 0
# while count < 10:
#     count += 1
#     if count == 5:
#         continue
#     print(count)



# калькулятор цикл
# while True:
#     num1 = int(input('1чи санды жаз : '))
#     num2 = int(input('2чи санды жаз : '))
#     znak = input('Танда : +, -, *, / -  ')
#
#     if znak == '+':
#         print(num1 + num2)
#     elif znak == '-':
#         print(num1 - num2)
#     elif znak == '*':
#         print(num1 * num2)
#     elif znak == '/':
#         print(num1 / num2)
#
#
#     else:
#         break




# обратный отсчет цикла
# num = int(input('Сан жаз: '))
# count = 31
# while count > 1:
#     count -= 1
#     if count == 31:
#         continue
#     print(count)
# print('the end')


# положительный отсчет цикла
# num = int(input('сан жаз: '))
# count = 0
# while count < 100:
#     count += 1
#     if count == 100:
#         continue
#     print(count)
# ptint('the end')





# сбор данных и сумма в итоге
# sum = 0
# while True:
#     a = int(input('введи цифру:'))
#     sum += a
#     if a == 0:
#      break
# print(sum)


# таблица умножение циклом for
# num = int(input('Введите цифру: '))
# for i in range(1, 11):
#      print(f"{num} * {i} = {num * i}")


# сумма внутри листа
# salary = [200, 400, 100, 350, 650]
# ss = sum(salary)
# print(f'cумма {ss}')


# salary = [200, 400, 100, 350, 650]
# total = 0
# for i in salary:
#     total += i
#
# print(f'Summa: {total}')




 # макс число в листе
# salary = [200, 400, 100, 350, 650,]
# for i in salary:
#     if i < 650:
#         continue
# print(i)


# salary = [200, 400, 100, 350, 650]
# max_number = 0
# for i in salary:
#     if i > max_number:
#         max_number = i
# print(f'max:{max_number}')




# минимальное число определение
# salary = [200, 400, 100, 350, 650]
# min_number = 999999
# for i in salary:
#     if i < min_number:
#         min_number = i
# print(f'min:{min_number}' )




# банкомат команды
# pin_code = 9963
# wallet = 1000
#
# pin = int(input('введите пин код: '))
# if pin != pin_code:
#     print('неправильный пин код')
# else:
#     while True:
#         print('1 - посмотреть счет')
#         print('2 - положить деньги')
#         print('3 - снять деньги')
#         print('4 - выйти')
#
#         go = int(input('выберите действие: '))
#         if go == 1:
#           print(wallet)
#         elif go == 2:
#            howm = int(input('сколько хотите положить?: '))
#            wallet += howm
#         elif go == 3:
#            howmm = int(input('сколько хотите снять?: '))
#            if howmm > wallet:
#                 print('недостаточно средств')
#            else:
#               wallet -= howmm
#
#         elif go == 4:
#            print('выход успешно выполнен')
#            break



# умножение чисел на свои индекса
# tt = []
# index_number = (2, 4, 6, 7, 3)
# for i in range(len(index_number)):
#    tt.append(index_number[i])
# print(tuple(tt))



# a = []
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#         a.append(i * numbers[i])
# print(a)



# переварачивать слово
# a = input('соз жаз:').title()
# print(a[::-1])



# четное не четное фолс тру
# number = int(input("san jaz: "))
# print(number % 2 != 0)


# уникальные
# num_elements = [1, 2, 2, 3, 4, 4, 5]
#
# uni_elements = list(set(num_elements))
# print(uni_elements)


# сравнение 2 листов и вывод похожих
# num1 = [1, 2, 3]
# num2 = [3, 4, 5]
#
# c_elements = list(set(num1) & set(num2))
#
# print(c_elements)



# минималтное число
# salary = [200, 400, 300, 250, 100, 500]
# min_num = salary[4]
# for i in salary:
#     if min_num > i:
#         min_num = i
# print(min_num)




# a = 2
# if a % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')
# s = 4
# if s % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')
# d = 7
# if d % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')
# f = 9
# if f % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')
# v = 5
# if v % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')
# j = 34
# if j % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')




# def greet():
#     print("Привет, мир!")
# greet()




# def change_numbers(a):
#     a.reverse()
#     print(a)





# def print_info(text, num):
#     for i in range(num):
#         print(text)
#
# print_info('Python', 2)
#
# print_info('Kyrgyzstan', 5)


# def word(list1, list2):
#     new_list = set(list1)
#     ss = new_list.intersection(list2)
#     print(list(ss))
#
#
# word(['Mers', 'BMW', 'Audi', 'Honda'], ['Tesla', 'BMW', 'Toyota', 'Honda'])




# def look_word(list1, list2):
#     lists1 = set(list1)
#     new_list = list(lists1.symmetric_difference(list2))
#     print(new_list)
#
#
# look_word(['Mers', 'BMW', 'Audi', 'Honda'], ['Tesla', 'BMW', 'Toyota', 'Honda'])

# [Mers, Audi, Tesla, Toyota]



# def numbers(*args):
#     set_number = set(args)
#     dd = sorted(set_number, reverse=True)
#     print(tuple(dd))
# numbers(9, 5, 6, 5, 3, 1)
#
# # (9, 6, 5, 3, 1)
#
#
# numbers(8, 2, 6, 2, 3, 8)
# # (8, 6, 3, 2)




# def two_list(list1,list2):
#     new_list = list1 + list2
#     print(tuple(new_list[::-1]))
#
#
# two_list(['mers', 'bmw', 'audi'], ['lion', 'sheep', 'horse'])

# (lion, sheep, horse, mers, bmw, audi)


# def two_list(a, b):
#     for i in a:
#         b.append(i)
#     print(tuple(b))
#
# two_list(['mers', 'bmw', 'audi'], ['lion', 'sheep', 'horse'])







# def duble_nums(nums):
#     ls = []
#     dd = nums[::-1]
#     for i in dd:
#         ls.append(i * 2)
#     print(tuple(ls))
#
#
# duble_nums([2, 4, 3, 7, 9, 8, 1])
#
# # (2, 16, 18, 14, 6, 8, 4)




# def full_name(name):
#     for i in name:
#         print(i.upper())
#
# full_name('Adilet')


# def max_number(*args):
#     jj = 0
#     for i in args:
#         if i > jj:
#             jj = i
#     print(f'max number : {jj}')
# max_number(2, 4, 52, 78,59, 8)


# def min_number(*args):
#     ab = args[0]
#     for i in args:
#       if i < ab:
#         ab = i
#     print(f'min number: {ab}')
#
# min_number(2, 4, 52, 78,59, 8)
#
# # min number : 2
#
# min_number(1, 90, 52, 78,59, 8)
# # min number : 1




# def index_number(*args):
#     ls = []
#     for i, s in enumerate(args):
#         ls.append(i * s)
#     print(tuple(ls))
#
#
# index_number(0, 5, 6, 3, 7, 9)
#
# (0, 5, 12, 9, 28, 45)



# def many_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)
#
#
# many_numbers(23, 45, 67, 89, 12, 2, 167)




# функция лямда
# lambda_f = lambda s, f: print(s + f)
#
#
# lambda_f(2, 5)
# # 7
# lambda_f(6, 90)
# #96



# палиндром с помощью функции
# def palindrom(text):
#     if text == text[::-1]:
#         print('Палиндром')
#     else:
#         print('Палиндром эмес')
# palindrom = lambda text: print('Палиндром') if text == text[::-1] else print('Палиндром эмес')
#
# palindrom('казак')
# palindrom('python')
# palindrom('car')
# palindrom('madam')




# палиндром с помощью функции
# def sandar(num):
#     if num % 2 == 0:
#         print('Жуп сан')
#     else:
#         print('Так сан')

# sandar = lambda num: print('Жуп сан') if num % 2 == 0 else print('Так сан')
#
# sandar(2)
# sandar(5)
# sandar(4)
# sandar(9)
# sandar(8)
# sandar(1)
# sandar(6)




# сумма с помощью функции
# def fgdsfsvsd(*args):
#     ss = sum(args)
#     print(ss)

# fgdsfsvsd = lambda *args: print(sum(args))
#
# fgdsfsvsd(2, 3, 45,6, 78)
# fgdsfsvsd(456, 78,52 ,78)
# fgdsfsvsd(3, 56, 1)




# def full_name(s):
#     for j in s:
#         print(j.upper())

# full_name = lambda s: [print(j.title()) for j in s]
#
# full_name('Altyn')




# def anagrama(word1, word2):
#     if sorted(word1) == sorted(word2):
#         print('Анаграма')
#     else:
#         print('Анаграма эмес')

# anagrama = lambda word1, word2: print('Анаграма') if sorted(word1) == sorted(word2) else print('Анаграма эмес')
#
# anagrama('сон', 'нос')
# # Анаграма
# anagrama('кино', 'кони')
# # Анаграма
# anagrama('книга', 'мудрость')
# # Анаграма эмес



# check_number = lambda i: print('он сан') if i > 0 else  print('терс сан')
#
# check_number(-21)
# check_number(1)
# check_number(987)
# check_number(-78)
# check_number(-34)

# терс сан
# он сан
# он сан
# терс сан
# терс сан



# words = lambda i: [print(car) for car in i[::-1]]
#
# words(['toyota', 'mers', 'Land Cruiser', 'matiz'])
#
# # matiz
# # Land Cruiser
# # mers
# # toyota




# print_info = lambda word, count: [print(word) for _ in range(count)]

# print_info('python', 3)
# print_info('car', 2)

# python
# python
# python
#
# car
# car



# my_laptops = lambda x: [print(f'{i} {laptop}') for i, laptop in enumerate(x)] + [print()]
#
# my_laptops(['Acer', 'Asus', 'HP'])
# my_laptops(['Lenovo', 'Acer', 'Asus'])

# 0 Acer
# 1 Asus
# 2 HP
#
# 0 Lenovo
# 1 Acer
# 2 Asus





# class Mashina:
#     def init(self, title, model, marka, price, color, millage, type_fuel):
#         self.title = title
#         self.model = model
#         self.marka = marka
#         self.price = price
#         self.color = color
#         self.millage = millage
#         self.type_fuel = type_fuel
#
#     def show_info(self):
#         return f'Название: {self.title}, Модель: {self.model},  Марка: {self.marka}, Цена: {self.price}, Цвет: {self.color}, Пробег: {self.millage}, Тип топлива: {self.type_fuel}'
#
#
# car1 = Mashina('Продаю машину Bmw', 'M5', 'BMW', 100000, 'черный', 27000, 'бензин')
# car2 = Mashina('Продаю Lexus', 600, 'Lexus', 50000, 'белый', 48000, 'бензин')
#
# print(car2.title)
# print(car2.show_info())






# class Computer:
#     def __init__(self, name, model, price, color, year):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.color = color
#         self.year = year
#
#     def show(self):
#         return f'Название: {self.name}, Модель: {self.model}, Цена: {self.price}coм, Цвет: {self.color}, Год выпуска {self.year}'
#
# com1 = Computer('Продаю ноутбук Asus', 'Asus', 67000, 'silver', 2024)
# print(com1.name)
# print(com1.show())




# class Computer:
#     def __init__(self, name, model, price, color, year):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.color = color
#         self.year = year
#
#     def show(self):
#      return f'{self.name}, Модель: {self.model}, Цена: {self.price} сом, Цвет: {self.color}, год: {self.year}'
#
#
# com1 = Computer('Asus', 'Rag2', 67000, 'silver', 2024)
# print(com1.name) # Asus
# print(com1.show()) # Asus, Rag2, 67000 сом , silver, 2024 год


# class Laptop:
#     def __init__(self, name, model, price, color, year, starage):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.year = year
#         self.starage = starage
#
#     def show(self):
#         return f'{self.name} {self.price} сом, {self.color} {self.year} год, {self.starage}гб'
#
# lab1 = Laptop('Lenovo', 'Rag2', 67000, 'silver', 2024, 512)
#
# print(lab1.name)  # Lenovo
# print(lab1.show())  # Lenovo, Rag2, 67000 сом , silver, 2024 год, 512 гб





# class Computer:
#     def __init__(self, name, model, price, color, year):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.color = color
#         self.year = year
#
#     def show(self):
#         return f'{self.name}, Модель: {self.model}, Цена: {self.price} сом, Цвет: {self.color}, год: {self.year}'
#
#
# com1 = Computer('Asus', 'Rag2', 67000, 'silver', 2024)
#
# print(com1.name) # Asus
# print(com1.show()) # Asus, Rag2, 67000 сом , silver, 2024 год
#
#

# наследование
# class Laptop(Computer):
#     def __init__(self, name, model, price, color, year, storage):
#         super().__init__(name, model, price, color, year)
#         self.storage = storage
#
#     def show(self):
#         return f'{self.name}, Модель: {self.model}, Цена: {self.price} сом, Цвет: {self.color}, год: {self.year}, память: {self.storage}гб'
#
#     # pass
# lab1 = Laptop('Lenovo', 'Rag2', 67000, 'silver', 2024, 512)
#
# print(lab1.name) # Lenovo
# print(lab1.show()) # Lenovo, Rag2, 67000 сом , silver, 2024 год, 512 гб




# class UserProfile:
#     def __init__(self, first_name, last_name, age, phone_number, work_place, gender, country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.phone_number = phone_number
#         self.work_place = work_place
#         self.gender = gender
#         self.country = country
#
#     def info(self):
#         return (f'имя: {self.first_name}, фамиля: {self.last_name}, возраст: {self.age}, '
#                 f'телефон: {self.phone_number}, работа: {self.work_place},'
#                 f' пол: {self.gender}, страна: {self.country}')
#
#
# user1 = UserProfile('Асель', 'Асанова', 23, '+9967778838383', 'Optima bank', 'Ж', 'KG')
#
# print(user1.first_name) # Асель
# print(user1.info())# 'Асель', 'Асанова', 23, '+9967778838383', 'Optima bank', 'Ж', 'KG'
#
#
# class  Author(UserProfile):
#     def __init__(self, first_name, last_name, age, phone_number, work_place, gender, country, city, height):
#         super().__init__(first_name, last_name, age, phone_number, work_place, gender, country)
#         self.city = city
#         self.height = height
#
#     def info(self):
#         return (f'имя: {self.first_name}, фамиля: {self.last_name}, возраст: {self.age}, '
#                 f'телефон: {self.phone_number}, работа: {self.work_place},'
#                 f' пол: {self.gender}, страна: {self.country}, город: {self.city}, рост: {self.height}')
#
#
# user1 = Author('Асан', 'Аманов', 34, '+9967778838334', 'ЦУМ', 'М', 'KG', 'Бишкек', 190)
#
# print(user1.first_name)  # Асан
# print(user1.info())  # 'Асан', 'Аманов', 34, '+9967778838334', 'ЦУМ', 'М', 'KG', 'Бишкек', 190




# 1. Основы Python
# 1.1. Типы Данных 8
# измен 3
# list [], [7], [98, 8, 'hbjk']
# set set(), {2, 3, 5, 7,3}
# dict {}, {'key': 'value'}
# неизмен 5
# int 2, 4, 65 22345
# float 1.7, 0.34, 12345.987
# bool True, False
# str '', 'sdfgdfg', 'book'
# tuple (), (2, 2)
#
# 1.2. Цикл
# for
# while
#
# break
# continue
# range
# enumerate
# sorted
# reversed
#
#
# 1.3. Функции
# def sdfghfddd()
# lambda
#
# *args
# **kwargs
#
# print()
# input
#
# if
# elif
# else
#
# 1.4. ООП
#
# Абстракция
# Наследование
# Полиморфизм
# Инкапсуляция
#
# class
# атрибут
# обьект
# метод
#
# 2. База Данных



# while True:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     print(num1+num2)
#     str = input('Для завершения нажмите Y')
#     if (str == 'y' or str == 'Y'):  break





numbers = ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
uni_elements = list(set(numbers))
print(uni_elements)