N, M=map(int, input().split())
 
factor=[]
#N의 약수 구하기
a=2
b=N
while a*a<=b:
    if b%a==0:
        factor.append(a)
        b//=a
    else:
        a+=1
if b>1:
    factor.append(b)
#M을 N의 약수로 나누어보며 최대공약수 구하기
mul=1
b=M
for i in range(len(factor)):
    if b%factor[i]==0: #M도 N의 약수로 나누어지면
        mul*=factor[i] #공약수로 곱함
        b//=factor[i]
 
print(mul) #최대공약수
print(N*M//mul) #최소공배수
