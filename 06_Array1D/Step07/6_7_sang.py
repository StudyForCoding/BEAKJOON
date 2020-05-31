c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0]
    count = 0
    for j in n[1:]:
        if j > avg:
            count += 1
    print("%.3f%%" %(count / n[0] * 100))
