sum = 0
for a in range(5):
    b = int(input())
    sum += b if b >= 40 else 40
print(int(sum/5))