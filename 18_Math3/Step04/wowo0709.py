n1,n2 = map(int,input().split())
gcd = 1
while(1):
    coprime = True
    for i in range(2,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            coprime = False
            n1=n1//i
            n2=n2//i
            gcd = gcd*i
            break
    if coprime:
        break
print(gcd)
print(gcd*n1*n2)