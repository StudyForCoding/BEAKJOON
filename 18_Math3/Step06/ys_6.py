def gcd(a, b): #분수 나눌 숫자 찾기(기약분수)
    while(b!=0):
        n=a%b
        a=b
        b=n
    return a

N = int(input())
M=list(map(int, input().split()))

for i in range(1, N):
    gcd2=gcd(M[0], M[i])
    print('{0}/{1}'.format(M[0]//gcd2, M[i]//gcd2)) #맨 처음 숫자를 다른 반지름으로 나누면 됨
