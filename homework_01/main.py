"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return list(map(lambda x: x ** 2, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def filter_numbers(numbers_list, arg):
    functions = {"odd": lambda x: x % 2 != 0,
                 "even": lambda x: x % 2 == 0,
                 "prime": is_prime,
                 }

    return list(filter(functions[arg], numbers_list))

