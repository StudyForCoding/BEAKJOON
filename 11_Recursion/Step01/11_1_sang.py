def factorial(n):  #틀림
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input())
print(factorial(n))
