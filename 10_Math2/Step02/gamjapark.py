def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())
count = 0
aa = []
for a in range(M, N + 1):
    if isPrimeNumber(a):
        aa.append(a)
if len(aa) > 1:
    print(sum(aa))
    print(min(aa))
else:
    print(-1)
