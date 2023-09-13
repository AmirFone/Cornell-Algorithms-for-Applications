from functools import reduce

def factorial_rec(n):
    """
    Returns the factorial of n using recursion.
    """
    def helper(n):
        if n == 0:
            return 1
        else:
            return n * helper(n-1)

    return helper(n)
def factorial_reduce(n):
    """
    Returns the factorial of n using functools reduce.
    """
    return reduce(lambda x, y: x * y, range(1, n+1))
