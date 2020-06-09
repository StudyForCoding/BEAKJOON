def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
count = 0
aaa = list(map(int, input().split()))
for a in aaa:
    if isPrimeNumber(a):
        count += 1
print(count)