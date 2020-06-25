n = int(input("입력: "))
i = 1
while True:
    if ((3 * (i ** 2)) - (3 * i) + 1) >= n:
        print("거리: %d"%i)
        break
    i += 1