# # This is first code in this course
# # Day one
# print('I love Python')
# """Printing hello world
# Writing comments here"""
# print('Hello World!!!')
# print('Test Repo')

# name = 'Python'
# print('Hello world ' + name)

# #Creating variables
# total = 100
# print(total)
# sum = total
# print(sum)
# a = total + 10
# print(a)
# total = 200
# print(total)
# a = b = c = 500
# print(a)
# print(b)
# print(c)
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# del total
# print(total) # This will raise error

# # String Literals
# name = 'Python'
# print(name)
# name_two = "Python"
# print(name_two)
# name_three = """I love Python"""
# print(name_three)
# name_three = """I
# love
# Python"""
# print(name_three)

# # Boolean Literals
# b = True
# print(b)
# c = False
# print(c)

# # Special Literal
# a = 10
# print(a)
# a = None
# print(a)
# del a

# # Number Data Type
# a = 10
# print(type(a))
# b = 2.5
# print(type(b))
# print(2e7)
# c = 10 + 11j
# print(type(c))

# # Print sep and end
# a = 10
# b = 20
# c = 30
# print(a, b, c)
# print(a, b, c, sep='')
# print(a, b, c, sep='|')
# print(a, b, c, sep='\n')
# print('I love Python')
# print('Yes')
# print('I love Python', end='')
# print('Yes')
# print('I love Python', end='.')
# print('Yes')
# print('Mondey', 'Tuesday', 'Wednesday')
# print('Mondey', 'Tuesday', 'Wednesday', sep=',', end=',')
# print('Thursday', 'Friday', 'Saturday', 'Sunday', sep=',')

# # Fundamental datatypes and immutability
# a = 10
# b = 10
# print(id(a))
# print(id(b))
# b = 20
# print(id(b))
# c = 30
# print(id(c))
# print(id(a + b))

# # Arithmetic operators
# a = 10
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(8 % 4)
# print(a // b)
# print(-a // b)
# print(10.0 // 4)
# print(a ** b)
# print(2 ** 3)

# # Assignment operators
# a = 10
# print(a)
# a += 5
# print(a)
# a -= 5
# print(a)
# a *= 2
# print(a)
# a /= 2
# print(a)
# a %= 3
# print(a)
# a **= 2
# print(a)
# a //= 3
# print(a)

# a = 5
# # Left shift operator
# print(a << 1)
# print(a << 2)
# # Right shift operator
# print(a >> 1)
# print(a >> 2)
# # Bitwise compliment operator
# print(~10)

# # and
# print(True and False)
# print(False and True)
# print(False and False)
# print(True and True)
# # or
# print(True or False)
# print(False or True)
# print(False or False)
# print(True or True)
# # not
# print(not False)
# print(not True)

# print(10 == 20)
# print(10 == 10)
# print(10 != 20)
# print(10 != 10)
# print(10 > 2)
# print(10 > 100)
# print(10 > 10)
# print(10 < 2)
# print(10 < 100)
# print(10 < 10)
# print(10 <= 10)
# print(10 >= 10)

# age = input("Enter your age: ")
# print(age)
# print(type(age))
# age = int(input("Enter your age: "))
# print(age)
# print(type(age))
# age = float(input("Enter your age: "))
# print(age)
# print(type(age))
# a = 5
# print(type(a))
# b = str(a)
# print(type(b))
# print(len('Python'))

# a = 10
# b = 20
# print('The value of a is {} and b is {}'.format(a, b))
# print('I love {} and {}'.format('apples', 'oranges'))
# print('I love {1} and {0}'.format('apples', 'oranges'))
# print('I love {first} and {second}'.format(first='apples', second='oranges'))
# x = 33.2314764
# print("the value of x is %4.2f" % x)

# x = 'Python'
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print('------------------')
# print(x[-6])
# print(x[-5])
# print(x[-4])
# print(x[-3])
# print(x[-2])
# print(x[-1])
# print(len(x))
# i = 0
# length = len(x)
# while i < length:
#     print((x[i]))
#     i += 1

# a = 'Python'
# # sting_name[start_index: end_index: step]
# print(a[1:4:1])
# print(a[1:4:2])
# print(a[1:4:])
# print(a[1::])
# print(a[:4:])
# print(a[::2])

# s1 = 'Python'
# s2 = 'programming'
# # Addition / concatenation (+)
# a = s1 + s2
# print(a)
# # Multiplication / repetition (*)
# b = s1 * 2
# print(b)

# a = 10 + 2 * 4
# print(a)
# x = 10 / 5 * 2
# print(x)
# def get_value(i):
#     print(i)
#     return i
# if __name__ == '__main__':
#     print(get_value(10) + get_value(20) + get_value(30))
# print(10 + 2 * 5)
# print((10 + 2) * 5)
# a = 10
# b = 20
# c = 30
# d = 40
# e = (a + b * c / d )
# print(e)
# e = ((a + b) * c) / d
# print(e)
# e = (a + b) * (c / d)
# print(e)

# age = 18
# if age > 18:
#     print("Welcome!")
# else:
#     print("You are not above 18. Sorry")

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# number = 0
# if first_number > second_number:
#     number = first_number
# else:
#     number = second_number
# print(f'{number} is bigger!')

# a = 0
# if a > 0:
#     print('Positive')
# elif a == 0:
#     print('Zero')
# else:
#     print('Negative')

# age = 61
# if age > 18:
#     if age > 60:
#         print('Senior citizen')
#     else:
#         print('Savings account')
# else:
#     print('Not eligible')

# a = int(input())
# b = int(input())
# c = int(input())
# num = 0
# if a > b and a > c:
#     num = a
# elif b > c:
#     num = b
# else:
#     num = c
# print('The largest number is: {}'.format(num))

# a = 'I love Python'
# for l in a:
#     print(l)

# for i in range(1, 10, 2):
#     print(i)

# for num in range(21):
#     if num % 2 == 0:
#         print(num)

# a = 1
# while a < 5:
#     print(a)
#     a += 1

# a = 5
# while a:
#     print(a)
#     a -= 1

# num = int(input('Enter number: '))
# num_sum = 0
# for n in range(num + 1):
#     num_sum += n
# print(num_sum)

# num = int(input('Enter number: '))
# num_sum = i = 0
# while i <= num:
#     num_sum += i
#     i += 1
# print(num_sum)

# a = 5
# while a:
#     print(a)
#     a = a - 1
#     if a == 2:
#         break
#     print('Inside while loop')
# print('Outside while loop')

# a = [1, 2, 3, 4, 5]
# for x in a:
#     print(x)
#     if x == 3:
#         break
#     print('Inside for loop')
# print('Outside for loop')

# a = 5
# while a:
#     print(a)
#     a = a - 1
#     if a == 2:
#         continue
#     print('End of the while loop')

# a = [1, 2, 3, 4, 5]
# for x in a:
#     print(x)
#     if x == 2:
#         continue
#     print('End of for loop')

# a = 1
# while a < 10:
#     pass
#
# a = []
# print(a)
# print(type(a))
#
# b = [1, 2, 3, 4, 5, 6]
# print(b)
# print(type(b))
#
# c = 'I love python programming'
# c_list = c.split()
# print(c_list)
# print(type(c_list))
#
# d = list(range(10, 20, 2))
# print(d)
# print(type(d))
#
# print(b[0])
# print(b[2])

# e = list(range(1, 12))
# print(e[0])
# print(e[-1])
#
# print(e)
# print(e[1:10])
# print((e[1:10:2]))
# print(e[1::2])
# print(e[10:1:-2])

# a = list(range(1, 12))
# print(a)
# a[1] = 100
# print(a)
#
# a[1:4] = [33, 34, 35]
# print(a)
#
# a.append(200)
# a.append(300)
# print(a)
#
# a.extend([2, 4, 10])
# print(a)
# b = [9, 99, 999]
# a.extend(b)
# print(a)
#
# a.insert(2, 1)
# print(a)
#
# del a[1]
# print(a)
#
# del a[1:3]
# print(a)
#
# a.remove(5)
# a.remove(9)
# print(a)
#
# a.pop(1)
# a.pop()
# print(a)
#
# a.clear()
# print(a)

# a = list(range(1, 12))
# a.append(1)
# print(len(a))
# print(a.count(1))
# print(a.index(1))
#
# a.sort()
# print(a)
#
# a.reverse()
# print(a)

# a = list(range(1, 12))
# print(a)

# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# for x in a:
#     print(x)

# n = len(a)
# for i in range(n):
#     print(i, " : ", a[i])

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
#
# d = a * 2
# print(d)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [1, 2, 4]
# d = [1, 2, 3]
# print(a == b)
# print(a == c)
# print(a == d)
#
# x = ['Python', 'programming']
# y = ['Python', 'PROGRAMMING']
# print(x == y)

# a = list(range(1, 12))
# print(1 in a)
# print(22 in a)
# print(1 not in a)
# print(22 not in a)

# a = [1, 2, 3]
# print(type(a))
# print(a)
#
# b = (1, 2, 3)
# print(type(b))
# print(b)
#
# c = ()
# print(type(c))
# print(c)
#
# d = (1)
# e = (1,)
# print(type(d))
# print(d)
# print(type(e))
# print(e)
#
# f = 1, 2, 3
# print(type(f))
# print(f)
#
# t = tuple(a)
# print(type(t))
# print(t)
#
# nt = (1, (2, 3))
# print(type(nt))
# print(nt)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print(a[1])
# print(a[-1])
#
# print(a)
# print(a[1:10:1])
# print(a[1:10:2])

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# a = (1, 2, 3, [4, 5, 6, 7, 8], 9, 10, 11)
# print(a)
# a[3][0] = 10
# print(a)

# a = 10
# b = 20
# c = 30
# d = 40
# t = a, b, c, d
# print(type(t))
# print(t)
#
# w, x, y, z = t
# print(w, x, y, z)

# a = {}
# print(type(a))
# print(a)
#
# a = {
#     1: 'Python',
#     2: 'Java'
# }
# print(type(a))
# print(a)
#
# a = dict()
# print(type(a))
# print(a)
#
# a = dict({
#     1: 'Python',
#     2: 'Java'
# })
# print(type(a))
# print(a)
#
# print(a[1])
# print(a.get(1))

# print(a)
# print(type(a))
# a[1] = 'Web'
# print(a)
#
# a[3] = 'DB'
# print(a)

# a = {
#     1: 'Web',
#     2: 'Java',
#     3: 'Database',
#     4: 'Ruby'
# }
# print(a)
# print(type(a))
#
# a.pop(1)
# print(a)
#
# a.popitem()
# print(a)

# del a[2]
# print(a)
#
# a.clear()
# print(a)
#
# del a
# print(a)

# a = {
#     1: 'Web',
#     2: 'Java',
#     3: 'Database',
#     4: 'Ruby'
# }
# print(a)
#
# print(1 in a)
# print(1 not in a)
# print(11 in a)
# print(11 not in a)

# a = {
#     1: 'Web',
#     2: 'Java',
#     3: 'Database',
#     4: 'Ruby'
# }
# print(a)
#
# for k, v in a.items():
#     print(f'{k}:{v}')
#
# for k in a:
#     print(f'{k} --> {a[k]}')

# a = {
#     1: 'Web',
#     2: 'Java',
#     3: 'Database',
#     4: 'Ruby'
# }
# print(a)
# print(len(a))
#
# print(a.get(1))
# print(a.get(1, 1000))
# print(a.get(11, 1000))
# print(a.get(11))
#
# print(a.keys())
# print(type(a.keys()))
# print(list(a.keys()))
# print(type(list(a.keys())))
# for i in a.keys():
#     print(i)
#
# print(a.values())
# print(type(a.values()))
# print(list(a.values()))
# print(type(list(a.values())))
# for i in a.values():
#     print(i)
#
# print(a.items())
# print(type(a.items()))
# print(list(a.items()))
# print(type(list(a.items())))
# for k, v in a.items():
#     print(f'{k} -> {v}')

# s = {1, 2, 3, 4, 5}
# print(s)
# print(type(s))
#
# s = {1, 2, 2, 3, 4, 5}
# print(s)
#
# s = {1, 2, 'Python', 3}
# print(s)
# print(type(s))
#
# l = [1, 2, 3, 4]
# print(type(l))
# s = set(l)
# print(s)
# print(type(s))

# a = {1, 2, 3}
# print(a, type(a))
#
# a.add(5)
# print(a)
#
# a.update([11, 22, 33])
# print(a)
# a.update(a, range(10))
# print(a)
#
# b = a.copy()
# print(b, type(b))

# a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# print(a, type(a))
#
# print(a.pop())
# print(a)
#
# a.remove(1)
# print(a)
#
# a.discard(11)
# print(a)
# a.discard(11)
#
# a.clear()
# print(a)

# a = {1, 2, 3, 4, 5, 6}
# b = {3, 4, 5, 6, 7, 8}
#
# c = a.union(b)
# print(c)
# d = a | b
# print(d)
#
# c = a.intersection(b)
# print(c)
# d = a & b
# print(d)
#
# c = a.difference(b)
# print(c)
# c = b.difference(a)
# print(c)
# d = a - b
# print(d)
# d = b - a
# print(d)
#
# c = a.symmetric_difference(b)
# print(c)
# d = a ^ b
# print(d)

# a = {1, 2, 3}
# print(1 in a)
# print(5 in a)
# print(1 not in a)
# print(5 not in a)

# a = 'I love \'Python\''
# print(a)
#
# a = 'It\'s time to write great code'
# print(a)
#
# a = 'I love \\ Python'
# print(a)
#
# a = 'I love \n Python'
# print(a)

# a = 'I love Python'
# print(a)
# a = """I
# love
# Python"""
# print(a)
# a = 'I \nLove \nPython'
# print(a)

# print(len('Python'))
#
# a = 'I love Python'
# print(a.index('o'))
# print(a.index('o', 4))
#
# print(a.count('o'))
# print(a.count('o', 4))
# print(a.count('o', 4, 6))
#
# print(a.lower())
# print(a.upper())
#
# print(a.split(' '))
# print(a.split(' ', 1))

# def print_hello():
#     print('Hello Python!')
#
# print_hello()
#
# def print_hello(name):
#     print('Hello', name)
#
# print_hello('JS')
# print_hello('World')
#
# def print_something(greeting, name):
#     print(greeting, name)
#
# print_something('Hi', 'John')
# print_hello(input('Enter name:'))
# print_something('Hi', input('Enter name:'))

# def user_info(name, age):
#     print(f'Hello {name} Your age is: {age}')
# user_info('Vlad', 33)
# user_info(age=33, name='Vlad')
# def user_info_default(name, age=24):
#     print(f'Hello {name} Your age is: {age}')
# user_info_default('Tom')
# user_info_default('Tom', 44)
#
# def greet(*name):
#     for s in name:
#         print(f'Hello {s}!')
#
# greet('Tom', 'Lita', 'Roma')

# def factorial(a):
#     if a ==0:
#         return 1
#     else:
#         fact = a * factorial(a - 1)
#         return fact
# print(factorial(20))
#
# def fact(number):
#     num = 1
#     while number != 0:
#         num *= number
#         number -= 1
#     return num
# print(fact(20))

# def addition(a, b):
#     temp = a + b
#     return temp
#
# def demo(a, b):
#     temp1 = a + b
#     temp2 = a - b
#     return temp1, temp2
#
# add = addition(3 , 4)
# print(add)
# print(demo(5, 3))
# x, y = demo(5, 3)
# print(x, y)

# l = [1, 2, 3]
# print(l.__iter__())
# i = l.__iter__()
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
#
# print(next(i))
# print(next(i))
# print(next(i))
#
# s = 'Hello Python'
# print(s.__iter__())
# print(iter(s))
# a = iter(s)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(next(a))
# print(next(a))

# class Counter:
#     def __init__(self, start, end):
#         self.current = start - 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.current += 1
#         if self.current < self.end:
#             return self.current
#         else:
#             raise StopIteration
#
# for c in Counter(3, 9):
#     print(c)

# def generator_demo():
#     i = 1
#     print('First')
#     yield i
#
#     i = i + 1
#     print('Second')
#     yield i
#
#     i = i + 1
#     print('Third')
#     yield i
#
# gen = generator_demo()
# # print(gen.__next__())
# # print(gen.__next__())
# # print(gen.__next__())
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# for i in generator_demo():
#     print(i)

# a = 100
# def outer():
#     a = 10
#     print('Outer', a, id(a))
#
# def inner():
#     b = 20
#     print('Inner', b, id(b))
#
# print(a, id(a))
# outer()
# inner()

# def demo():
#     print('From function:', a)
#
# a = 100
# print('From outside function', a)
# demo()

# def outer():
#     global a
#     a = 10
#     print('Outher:', a, id(a))
#
# a = 100
# outer()
# print('Main:', a, id(a))

# x = 100
# a = True
# b = False
# if x == 1 & (a & b):
#     print(x)
#     print(x * 2)

# x = 100
# a = True
# b = False
# a = x == 1 & (a & b)
# print(x)

# x = 100
# a = True
# b = False
# if x == 1 & (a & b):
#     print(x)
# print(x * 2)

# a = 'I Love Python Programming'
# print(a.count('o', 2))

# i = 2
# if i > 0:
#     print("#")
#     if i < 4:
#         print("#")
#     elif i < 3:
#         print('#')
#     elif i == 2:
#         print("#")
#     else:
#         print("#")
#
# else:
#     print("#")

# print(1 // 2)
# print(13. // -4)
# print(12. % -4)

# list = [[2 - i for i in range(2)] for j in range(2)]
# var = 0
# for i in range(2):
#     var += list[i][i]
# print(var)

# str = 'ThankS'
# str[5] = 's'
# print(str)

# var = 25.6
# var = int(var)
# print(var)

# print(9.5 // 3)

# fruit = "Mango",
# print(type(fruit))

# list = [1, 2, 3, 4, 5]
# print(list[list[-1]])

# def add(p, q, r, s=5):
#    return p + q + r + s
# print(add(p = 1, q = 2, r = 3))

# for num in range(2, 11, 3):
#    print(num, end = ",")

# print(23%4)

# print(type(3/2))
# print(type(3//2))

# age = 15
# print(not age > 14 and age < 16)

# d1 = dict({1: 'ONE', 2: 'TWO', 3: 'THREE'})
# print(d1)

# full_name = "jack-skate walker"
# print(full_name.title())

# t = tuple('Hello World')
# print(t[:-6])

# x = "None"
# if x:
#    print("Good morning")
# else:
#    print("Good Evening")

# def swap(num1, num2):
#    temp = num1;
#    num1 = num2;
#    num2 = temp;
# num1 = (2)
# num2 = (5)
# swap(num1, num2)
# print(num1 , num2)

# def f(i):
#     if i > 2:
#         return i
#     else:
#         return f(0) * f(3)
# print(f(2))

# tupl1 = (1, 2, 3)
# tupl2 = ("Apples", "Bananas")
# tupl3 = (tupl1 + tupl2)
# print(tupl3)
# tupl4 = tupl1 + tupl2
# print(tupl4)

# print(end='',sep='@@')

# print(5** 2 ** 0 ** 1)

# d = {'r': 2, 'p': 4, 'q': 5}
# print(sorted(d))
#
# a= [1,2,3,4,5]
# print(a.index(3))

# def swap(a, b):
#     a, b = b, a
#     return (a, b)
#
#
# a = "Python2"
# b = "Python3"
# a, b = swap(a, b)
# print(a, b)

# x = ['welcome', 'to' ,'Python']
# y = ['welcome', 'to' ,'Python']
# x.pop(1)
# print(x)
# y.pop()
# print(y)

# x = 10.5
# y = "ONE"
# print(int(x))
# print(int(y))

# a = 1
# b = 1
# print(a^b)

# x = {'r':2,'p':4,'q':5, 's':3}
# x.pop('s')
# print(x)
# x.pop(3)
# print(x)

# tupl = (1, 2,3,4,5)
# print(tupl[-3])

# print = "Hi"
# print (print)

# print(4 ** 2)
# print(4 ** 2.)
# print(4. ** 2)
# print(4.0 ** 2.0)

# def swap(a, b):
#     a, b = b, a
#     return (a, b)
#
#
# a = "Python2"
# b = "Python3"
# a, b = swap(a, b)
# print(a, b)

# french_greeting = 'Bonjour'
# for i in french_greeting:
#     if i == 'o':
#         pass
#     print(i)
# else:
#     print('Madam')

# a = 0
# while (a < 5): a += 2
# print(a)

# val = ("hi","hello","bye")
# val.pop()

# print(12/3)

# x = (("Python", 2, (5,6,7)), ("Java", 3, (7,8,9)),("Perl", 4, (2,3,4)))
# print(x[1][2])

# print(not 'Male')
# print(not None)
# print(None)

# dict1 = {12:35,13:26,49:24,55:46,90:20}
# dict2 = {56:68,35:15,25:28,32:39,65:40}
# output = dict1 > dict2
# print(output)

# dict1 = {'Name': 'Samuel'}
# dict2 = {'Age': 20}
# dict3 = dict1 + dict2
# print(dict3)

# for ch in 'apple':
#    if ch != 'p' and ch != 'e':
#         continue
#    print(ch,end="")

# d = {"x":"xx","xx":"None"}
# key = "x"
# key = d[key]
# key = d[key]
# print(key)

# def materials(x):
#     x[-2] = "Chair"
# household = ["fridge", "shoe rack", "Study Table"]
# materials(household)
# print(household)

# list = ['p', 'q', 'r']
#
# def func(char):
#     char.pop()
#     char.append('s')
#     print(char)
#
#
# func(list)
# print(list)

# def func():
#     global a
#     print(a)
#     a = 'College'
#     print(a)
#
#
# a = 'School'
# func()
# print(a)

# mixed_list = [65,"A",66,"B",67,"C"]
# mixed_list.sort()
# print(mixed_list)

# for num in range(8,6,-1):
#    print(("*"))

# def outer():
#    lst = [1,2,3,4,5,6]
#    def inner():
#        lst[-1] = 0
#        print(lst)
#    inner()
#    print(lst)
# outer()

# ch = 'circus'
# if 'ir' in ch: print(ch)

# List = ['p','q']
# List.append('r')
# List.append([10,20,30])
# List.extend([200,500])
# print(List)

# input = 3
# if ( input == 1 ):
#    print("1")
# elif ( input == 2 ):
#    print("2")
# print("3")


# l1 = ['A','a','B','b']
# l1.sort()
# print(l1)

# print("Python is a",print("High level"),print("OOP"),print("NOT ML"))

# w = [1, 1]
# x = w
# y = w.copy()
# z = list(w)
# w[0], w[1] = 2, 3
#
# print(" w : ", w)
# print(" x : ", x)
# print(" y : ", y)
# print(" z : ", z)

# x = 123
#
#
# def sum_of_digits(y):
#     sum = 0
#     while (y != 0):
#         sum = sum + int(y % 10)
#         y = int(y / 10)
#     print(sum)
#
#
# sum_of_digits(x)

# k = 1
# for i in range(1,2):
#     for j in range(-1,2):
#         if i ==j:
#             k +=1
#         else:
#             break
# print(k)

# a = 1, 2, 3,
# b = 'a', 'b', 'c'
# print(a + b)
# print(type(a))
# print(type(b))
#
# t = ()
# print(type(t))

# List1 = [1, 2, 3, 4, 5]
# print(3 in List1[2:7]))
# print(List1.index(List1[-1]) == 4)
# print(List1.index(List1[-1]) == 0)
# print(len(List1[0:1]) == 0)

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(7))

# n = 5
# sum_of_numbers = (n * (n + 1)) // 2
# print("Sum of first", n, "natural numbers is:", sum_of_numbers)

# dict = {"Dalserver":12,"Ausserver":14,"Londonserver":16}
# for i in dict.items():
#     print(i[0], end="")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# result = factorial(5)
# print("Factorial is", result)

# num = 3//2 * 3
# if num > 3:
#     print("Hello World")
# else:
#     print("Something Different")

# numbers = [1, 2, 3, 4, 5]
# new_numbers = [x**2 for x in numbers if x % 2 == 0]
# print(new_numbers)


# students = [
#     {'grade': 6, 'first_name': 'Vladimir', 'last_name': 'Zapryanov'},
#     {'grade': 6, 'first_name': 'Vladimir', 'last_name': 'CZapryanov'},
#     {'grade': 3, 'first_name': 'Ivan', 'last_name': 'Georgiev'},
#     {'grade': 2, 'first_name': 'Georgi', 'last_name': 'Ivanov'},
#     {'grade': 5, 'first_name': 'Mario', 'last_name': 'Dimitrov'},
#     {'grade': 6, 'first_name': 'Vladimir', 'last_name': 'EZapryanov'},
#     {'grade': 6, 'first_name': 'AVladimir', 'last_name': 'EZapryanov'},
#     {'grade': 5, 'first_name': 'Maria', 'last_name': 'Ivanova'}
# ]
#
# sorted_students = sorted(students, key=lambda x: (-x['grade'], -ord(x['last_name'][0]), x['first_name']))
# for student in sorted_students:
#     print(student)

# L = [1, 2, 3, 4, 5]
# L*2
# print(L)

# L = [1, 2, 3, 4, 5]
# L1 = L
# L.append(7)
# del L
# print(L1)

# try:
#     1/0
# except ArithmeticError:
#     print("It is wrong")
# except ZeroDivisionError:
#     print("Any number cannot be divided by zero")

# my_tuple = (1, 2, 3, 4)
# print(len(my_tuple))

# x = 15
# y = 10
# z = 5
# if x > y:
#     if y > z:
#         result = "A"
#     else:
#         result = "B"
# else:
#     result = "C"
# print(result)

# values = []
# for i in range(1, 4):
#     values.append(i)
#     print(values)

# for x in range(4):
#     if x == 3:
#            break
#     print(x)
#
# else:
#     print("Done")

# a = 1
# for i in range(2, 5):
#     if 2 * i > 4:
#         a += 1
# else:
#     a -= 1
# print(a)

# a = -1
# for i in range(1, 3):
#     for j in range(1, 2):
#         if i == j:
#             a += 1
#     else:
#         a += 1
# print(a)

# the_data = ['data', -1, 2.718281828459]
# print('data' in the_data)
# print(the_data.index(-1) > 0)
# print(int(the_data[2]))

# a = tuple()
# b = (2,)
# print(type(a), type(b))
# c = a + b
# print(c , type(c))

# n = [4, 3, 2, 1]
# # print(n[n[0]])
# print(n[n[3]])
# # print(n[4])
# print(n[3:5])

# power = 1
# while power < 5:
#     power += 1
#     print('@', end='')
#     if power == 3:
#         break
# else:
#     print('@')

# def process(data):
#     data = [1, 2, 3]
#     return data
# measurements = [0 for i in range(3)]
# process(measurements)
# print(measurements[-2])

# n = 1_999
# print(type(n))

# train_speed = {'FlyingScotsman': 201, 'TGV': 320, 'Shinkansen': 320}
# for train in train_speed.items():
#     print(train[0], end='')

# list = [False, True, '2', 3, 4, 5]
# b = 0 in list
# print(b)

# x = [0, 1, 2]
# x.insert(0, 1)
# del x[1]
# print(sum(x))

# print(list('hello'))

# str1 = 'Vlad'
# str2 = str1[:]
# print(id(str1), id(str2))

# data = ((1, 2),) * 7
# print(data)
# print(len(data[3:8]))

# l = [1, 2, 3, 4, 5]
# l.reverse()
# print(l)

# data = {'a': 1,
#         'b': 2,
#         'c': 3}
# print(data['a', 'b'])

# l = []
# for i in range(-1, -2):
#     a = i
#     l.append(a)
# print(l)

# nums = [1, 2, 3]
# data = ('1',) * (len(nums) - nums[::-1][0])
# print(type(data))
# print(nums[::-1])
# print(('1',) * 2)

# l = [2, 7, 1, 4]
# # l.sort()
# sorted(l)
# print(sorted(l))

# data = ['abc', 'def', 'abcde', 'efg']
# print(max(data))

# list = ['Peter', 'Paul', 'Mary']
# def l(data):
#     del data[1]
#     data[1] = 'Jane'
#     return data
# print(l(list))

# data = {'1': '0', '0': '1'}
# for d in data.values():
#     print(d, end=' ')

# data = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14 , 15, 16]
# ]
# for i in range(0, 4):
#     print(data[i].pop(), end='')

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# x[::2] = 10, 20, 30, 40, 50, 60
# print(x)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(crates)
# print(jars)
# print(box)
# print(len(crates['box']))

# data = [1, 5, 10, 19, 55, 30, 55, 99]
# data.pop(5)
# data.remove(19)
# data.remove(55)
# data.remove(55)
# print(data)

# l1 = [1, 2, 3]
# for v in range(len(l1)):
#     l1.insert(1, l1[v])
# print(l1)

# t = (('A', 1), ('B', 2), ('C', 3))
# d = dict(t)
# print(d)

# data = {}
# data[1] = 1
# data['1'] = 2
# data[1.0] = 4
# res = 0
# for d in data:
#     num = data[d]
#     res += num
# print(res)
# print(data[1])

# z = 3
# y = 7
# x = y < z and z > y or y > z and z < y
# print(x)

