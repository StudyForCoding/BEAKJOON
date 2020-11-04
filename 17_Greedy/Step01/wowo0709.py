n,k = map(int,input().split())
money = []
for i in range(n):
    money.append(int(input()))
count = 0
while k != 0:
    for i in range(len(money)-1,-1,-1):
        if k - money[i] <0:
            continue
        k = k - money[i]
        count +=  1
        break
print(count)