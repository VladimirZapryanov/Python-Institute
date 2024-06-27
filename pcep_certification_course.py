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

n = float(input('Enter the number: '))
less_then = n > 100
print(less_then)