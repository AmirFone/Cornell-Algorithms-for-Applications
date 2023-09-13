from functools import reduce

def square_all(numbers):
    """
    Returns a list of squares of all numbers.
    """
    return [num ** 2 for num in numbers]

def filter_even(numbers):
    """
    Filters and returns only the even numbers from the list.
    """
    return [num for num in numbers if num % 2 == 0]

def product_of_all(numbers):
    """
    Returns the product of all numbers in the list using reduce.
    """
    return reduce(lambda x, y: x * y, numbers)
