import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance1 = math.sqrt(((x2-x1)**2) + ((y2 - y1)**2))
    distance2 = r1 + r2
    distance3 = abs(r2 - r1)

    if distance1 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance1 == distance2 or distance1 == distance3:
        print(1)
    elif distance1 > distance2 or distance1 < distance3:
        print(0)
    elif distance3 < distance1 < distance2:
        print(2)