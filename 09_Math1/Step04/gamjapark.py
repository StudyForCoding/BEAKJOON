N = int(input("입력: "))
i = 1
while True:
    sum1 = int(((i + 1) * i) / 2)
    if N <= sum1:
        break
    i += 1
a = 1
b = i
while sum1 != N:
    a += 1
    b -= 1
    sum1 -= 1

if i % 2 == 0:
    print("값: %d/%d"%(b, a))
else:
    print("값: %d/%d"%(a, b))