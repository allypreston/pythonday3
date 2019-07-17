# functions can be in two states
# - definition/ declaration
# *** line def line is a function declaration
# - invocation
# *** the block of code that runs the operations
# A class is an overarching thing that holds a series of functions
# a variable only stored inside the function is known as a local variable


class Calculator:


    def add(num1, num2):
        return num1 + num2


    def subtract(num1, num2):
        return num1 - num2


    def multiply(num1, num2):
        return num1 * num2


    value1 = 5 + 5
    print(value1)

    user_value1 = int(input('Enter first value > '))
    user_value2 = int(input('Enter second value > '))


    result1 = add(user_value1,user_value2)
    print(result1)

    value2 = 6 - 5
    print(value2)

    value3 = 7 // 2
    print(value3)

    value4 = 8 + 8
    print(value4)

    value4 = add(8,8)
    print(value4)


def area_of_circle(radius):
    pi = 3.142
    return pi*radius * radius

result = area_of_circle(int(input('please input a radius')))
print(result)