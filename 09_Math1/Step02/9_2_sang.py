n = int(input())
result = n // 5
c = n % 5
if c == 0:
    print(result)
elif c == 1:
    print(result + 1)
elif c == 2:
    result -= 2
    if result < 0:
        print(-1)
    else:
        print(result + 4)
elif c == 3:
    print(result + 1)
elif c == 4:
    result -= 1
    if result < 0:
        print(-1)
    else:
        print(result + 3)
