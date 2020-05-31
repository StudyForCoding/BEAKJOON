a = int(input())
b = int(input())
c = int(input())
r = str(a * b * c)
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in r:
    l[int(i)] += 1
for i in range(10):
    print(l[i])
