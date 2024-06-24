import random

from learn_everything_ai_functions import poly

a = 2
b = 3
print(a + b)

print((2+4+6)*3-12/3)
print(8**2)

print((2.0+4.0+6.0)*3.0-12.0/3.0)
print(8.0**2)

print(7.0/4.0)
print(7/4)

print(34+1.0)

print(float(1))
print(int(3.678))

x = 3
y = 2
z = 7
a = x*y*z
print(a)

print("spam" + " " + "eggs and spam")
print("spam "*4 + "beans and spam")

a = 1
b = 1.0
c = "1.0"
print(type(a))
print(type(b))
print(type(c))

print(2**3)
print(pow(2, 3))

a = [0, 1, 2]
a.append(3)
print(a)

d = 3 + 5j
e = 1 + 1j
print(type(d))
print(d.real)
print(d.imag)
print(abs(d))
print(d*e)

print(1.0/3.0)
print(1000000000*100000000000)

a = 1.123456789
print(a)
print("a = %.2f" % a, "cms")
a = 1.23
b = 123.45
print("a = %5.2f" %a, "b = %.4e" %b)

# a = input("Input a number: ")
# print(a)
# b = input("Input your name: ")
# print(b)

a = [3, 54, 26, 90]
print(a)
b = [3, 54, 'llama', a]
print(b)
print(a[0])
print(b[3])
print(b[3][2])
print(a[-1])
print(a[-2])
print(len(a))
a[2] = 'gecko'
print(a)
a = [12, 23, 34, 45, 56, 67, 78]
print(a[3:6])
print(a[3:])
print(a[:3])
c = a+b
print(c)
c.append('vlad')
print(c)
c.insert(3, 99)
print(c)
print(3 in c)
print(7 in c)
a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
print(c)
d = map(float, a)
print(d)

a = (1, 2, 3)
print(a)
print(type(a))
print(a[1])

a = "This parrot is dead"
print(a[5:11])
print(a.find("This"))
print(a.find("dead"))
print(a.find("vlad"))
print(a.split(" "))

phonebook = {}
phonebook['Fred'] = '12345'
phonebook['Claire'] = '0234 7432'
print(phonebook)
print(phonebook['Claire'])
print(len(phonebook))

# a = float(input('Please enter a positive number: '))
# b = float(input('Please enter one more positive number: '))
# if a < 0 or b < 0:
#     print('One of numbers is negative')
#     print('That is not what I asked for')
# elif a > 0 and b > 0:
#     print('Thank you')
#     print('That is a positive numbers')
# else:
#     print('That looks like zero to me')

# number = float(input('Please enter a positive number less than 10: '))
# while number < 0 or number > 10:
#     number = float(input('Please enter a positive number less than 10: '))
# print('Thank you. That number is fine.')

cheese_list = ['Wensleydale', 'Stilton', 'Danish Blue', 'Red Leicester', 'Brie']
for cheese in range(0, len(cheese_list)):
    print('Do you have some', cheese_list[cheese], '?')
for cheese in cheese_list:
    print(f'Do you have some {cheese} ?')

for number in range(10):
    print(f'The number: {number} It is square: {number**2}')

# x_value = input('Enter a value for x: ')
# while x_value != 'stop':
#     x_value = float(x_value)
#     y_value = poly(x_value)
#
#     print(f'The value of the polynomial is: {y_value}')
#     x_value = input('Enter a value for x: ')

# a = float(input('Enter a number: '))
# b = float(input('Enter another number: '))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('The second number must not be zero')


f = open('temp.txt', 'a')
number = random.random()
f.write(f'{number}\n')
print(number)
number = random.uniform(1, 1000000)
print(number)
f.write(f'{number}\n')
f.close()