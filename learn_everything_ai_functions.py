def poly(x):
    y = x**3 - 7*x**2 + 14*x - 5.0
    return y


#Numbers must be write separated by commas
def separated_numbers(numbers):
    nums_str = numbers.split(',')
    nums = []
    try:
        for n in nums_str:
            nums.append(int(n))
    except:
        nums = []

    return nums