n = int(input())
f = 0
sum = 0
while True:
    sum += 6 * f
    if sum >= (n - 1):
        break
    else:
        f += 1
print(f + 1)
