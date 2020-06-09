import math
def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

M, N= map(int, input().split())

count = 0

for a in range(M, N + 1):
    if isPrimeNumber(a):
        print(a)
