n = int(input())
a, b = n // 10, n % 10
temp = a + b
count = 1
while b * 10 + temp % 10 != n:
    a, b = b, temp % 10
    temp = a + b
    count += 1
print(count)
