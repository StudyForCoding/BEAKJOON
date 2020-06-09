M = int(input())
N = int(input())

total =[]
def primenum(i):
    for a in range(2,i):
        if i%a==0:
            return 0
    total.append(i)

for i in range(M,N+1):
    if i >1:
        primenum(i)
if len(total)>1: print(sum(total),min(total))
else: print(-1)
    