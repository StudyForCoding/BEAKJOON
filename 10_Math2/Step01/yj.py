N = int(input())
num = map(int,input().split())
total=0
def primenum(i):
    for a in range(2,i):
        if i%a==0:
            return 0
    return 1

for i in num:
    if i >1:
        total+=primenum(i)
print(total)
    