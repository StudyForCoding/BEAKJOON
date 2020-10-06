n = int(input())
counts = [1,2,0]
for i in range(2,n):
    counts[2] = (counts[0] + counts[1])%15746
    if i%2 == 0:
        counts[0] = counts[2]
    else:
        counts[1] = counts[2]
if n==1:  print(1)
elif n==2:  print(2)
else:  print(counts[2])