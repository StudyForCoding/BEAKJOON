n = int(input())
n0 = 1
count = 0
while n0 != 0:
    n5 = (n // 5) - count
    n3 = ((n % 5) + count * 5) // 3
    n0 = ((n % 5) + count * 5) % 3
    count += 1
    if n5 < 0:
        rst = -1
        break
    else:
        rst = n5 + n3
print(rst)
