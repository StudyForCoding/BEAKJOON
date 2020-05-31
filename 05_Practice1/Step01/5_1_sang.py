s = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    s += a
print(int(s / 5))
