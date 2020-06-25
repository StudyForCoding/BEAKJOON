T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 1
    count = 0
    while True:
        pow_s = n**2
        min_s = pow_s - n + 1
        max_s = pow_s + n
        if min_s <= distance <= max_s:
            if min_s <= distance <= pow_s:
                count = (n << 1) - 1
            else:
                count = n << 1
            break
        n += 1
    print(count)