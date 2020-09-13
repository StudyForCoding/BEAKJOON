n = int(input())
num = []
for m in range(n):
    num.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if num[min_index]>num[j]:
            min_index = j
    num[min_index], num[i] = num[i], num[min_index]

for nu in num:
    print(nu)