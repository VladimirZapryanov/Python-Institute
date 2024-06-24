from learn_everything_ai_functions import separated_numbers

# x = float(input())
# y = (x**2) - 1
#
# print(f'{y:.3f}')


# list_with_names = ['Vlad', 'Ivan', 'Viki', 'Ceco', 'Mario', 'Misho', 'Petur', 'Bobi', 'Niki', 'Kiro']
# list_with_ages = [20, 21, 22, 33, 44, 55, 66, 34, 25, 26]
#
# name = input('Enter a name: ')
# friends_count = len(list_with_names)
# line_in_list = list_with_names.index(name)
# birth_year = list_with_ages[line_in_list]
#
# print(f'You have {friends_count} friends')
# print(f'{name} is number {line_in_list} in your list')
# print(f'{name} is {birth_year} years old')


# friends_dict = {
#     'Vlad': 20,
#     'Ivan': 21,
#     'Viki': 22,
#     'Ceco': 33,
#     'Mario': 44,
#     'Misho': 55,
#     'Petur': 66,
#     'Bobi': 34,
#     'Niki': 25,
#     'Kiro': 26
# }
#
# name = input('Enter a name: ')
# while name not in friends_dict:
#     name = input('Enter a new name: ')
#
# friends_count = len(friends_dict)
# line_in_list = list(friends_dict.keys()).index(name)
# print(f'You have {friends_count} friends')
# print(f'{name} is number {line_in_list} in your list')
# print(f'{name} is {friends_dict[name]} years old')


# start_number = int(input('Enter start number: '))
# end_number = int(input('Enter end number: '))
# increment_number = int(input('Enter increment number: '))
#
# for number in range(start_number, end_number, increment_number):
#     print(f'Number: {number} Square: {number**2} Cube: {number**3}')


numbers = input('Enter the parameters separeted by commas: ')
sep_nums = separated_numbers(numbers)
print(f'The parameters are: {sep_nums}')