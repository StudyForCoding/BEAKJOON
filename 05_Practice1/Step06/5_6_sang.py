n = int(input())
for i in range(n):
    a, b = n // 2, n % 2
    if b == 1:
        a += 1
    b = n - a
    for j in range(a):
        print('* ', end="")
    print()
    for j in range(b):
        print(' *', end="")
    print()
