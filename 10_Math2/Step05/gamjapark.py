import math
def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    for k in range(n // 2, 1, -1):
        r = n - k
        if isPrimeNumber(k) and isPrimeNumber(r):
            print("%d %d"%(k, r))
            break
