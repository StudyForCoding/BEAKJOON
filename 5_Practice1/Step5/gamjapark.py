n = int(input())
for i in range(n):
    print(" "*i + "*"*(n - i) + "*" * (n - i - 1))
for i in range(n, 1, -1):
    print(" "*(i - 2) + "*"*(n - i + 2) + "*"*(n - i + 1))