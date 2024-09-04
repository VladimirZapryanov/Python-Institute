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
