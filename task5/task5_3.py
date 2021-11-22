
"""
Task 3 with first fibonchy numbers

"""
def fib(n, x=[0]):

    if n == 0:
        return x
    elif  len(x) < 2:
        return fib(n - 1, x + [1])
    return fib(n - 1, x + [x[-1] + x[-2]])


if __name__ == '__main__':
    print(fib(5))
    print(fib(10)) 


