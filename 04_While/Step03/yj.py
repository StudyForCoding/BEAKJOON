N = int(input())
Num=N
n=0
num=0
while True:
    b = N//10
    c = N%10
    num = c*10+(b+c)%10
    n+=1
    N=num
    if Num==num:
        break
print(n)