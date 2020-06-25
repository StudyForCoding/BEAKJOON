a, b, v = map(int, input().split())
count = 0
day = 0
while count != v:
    count += a
    day += 1
    if count == v:
        break
    else:
        count -= b
print(day)
