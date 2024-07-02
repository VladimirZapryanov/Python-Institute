from time import sleep

print('Hello, World!')

print('Hello, Python!')
print('Vladimir')

print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

print('\\')

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

print("My name is", "Python.")
print("Monty Python.")

print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is ", end="")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("2")
print(2)

print(0o123)
print(0x123)

print('I\'m Monty Python.')
print("I'm Monty Python.")

print(True > False)
print(True < False)

print('"I\'m"\n""learning""\n"""Python"""')

print(2+2)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

print(14 % 4)
print(12 % 4.5)

print(-4 + 4)
print(-4. + 8)

print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)

print(9 % 6 % 2)
print(2 ** 2 ** 3)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

var = 1
print(var)
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

var = '3.8.5'
print('Python version: ' + var)

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

a = 3.0
b = 4.0
c = (a**2 + b**2)**0.5
print('c =', c)

john = 3
mary = 5
adam = 6
print(john,mary,adam, sep=",")
total_apples = john + mary + adam
print('Total number of apples:', total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)

var = 2
print(var)
var = 3
print(var)
var += 1
print(var)

var = "007"
print("Agent " + var)

# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# first_number = float(input('Please write first float number: '))
# second_number = float(input('Please write second float number: '))
# sum_result = first_number + second_number
# sub_result = first_number - second_number
# mul_result = first_number * second_number
# div_result = first_number / second_number
# print(f"{sum_result}\n{sub_result}\n{mul_result}\n{div_result}\nThat's all, folks")

var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)
var = 1  # Assigning 1 to var
print(var != 0)

# n = float(input('Enter the number: '))
# less_then = n > 100
# print(less_then)

## Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)

# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)

# plant_name = input('Enter plant name: ')
# if plant_name == 'Spathiphyllum':
#     print('Yes - Spathiphyllum is the best plant ever!')
# elif plant_name == 'spathiphyllum':
#     print('No, I want a big Spathiphyllum!')
# else:
#     print(f'Spathiphyllum! Not {plant_name}!')

# income = float(input("Enter the annual income: "))
# tax = 0
# if income <= 85528.0:
#     tax = income * 0.18 - 556.2
# elif income > 85528.0:
#     tax = 14839.2 + (income - 85528) * 0.32
# if tax < 0:
#     tax = 0
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

# year = int(input("Enter a year: "))
# year_is = ''
# if year < 1582:
#     year_is = 'Not within the Gregorian calendar period'
# elif year % 4 != 0 and year % 400:
#     year_is = 'Common year'
# else:
#     year_is = 'Leap year'
# print(year_is)

# # Store the current largest number here.
# largest_number = -999999999
#
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
#
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#
# # Print the largest number.
# print("The largest number is:", largest_number)

# # A program that reads a sequence of numbers
# # and counts how many numbers are even and how many are odd.
# # The program terminates when zero is entered.
#
# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
#
# user_number = int(input())
# while not user_number == secret_number:
#     user_number = int(input("Ha ha! You're stuck in my loop!"))
# print(secret_number)
# print('Well done, muggle! You are free now.')

# for i in range(2, 8, 3):
#     print("The value of i is currently", i)
#
# for n in range(1, 6):
#     print(f'{n} Mississippi')
#     sleep(1)
#
# print('Ready or not, here I come!')

# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# largest_number = -99999999
# counter = 0
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#
# largest_number = -99999999
# counter = 0
# number = int(input("Enter a number or type -1 to end program: "))
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# word = input('Enter the word or chupacabra to exit: ')
# while True:
#     if word == 'chupacabra':
#         break
#     word = input('Enter the word or chupacabra to exit: ')
# print("You've successfully left the loop.")

# user_word = input('Enter a word: ').upper()
# for l in user_word:
#     if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
#         continue
#     print(l)

# user_word = input('Enter a word: ').upper()
# word_without_vowels = ''
# for l in user_word:
#     if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
#         continue
#     word_without_vowels += l
# print(word_without_vowels)

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

for i in range(5):
    print(i)
else:
    print("else:", i)
