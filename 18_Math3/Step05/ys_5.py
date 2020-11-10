import math
N = int(input())
num = []
gcd = 0
for i in range(N):
    num.append(int(input()))

num.sort()

k=num[-1]-num[0] #가장 큰값에서 작은값 뺌-> 최대 약수?
div=[k]
for i in range(2, int(math.sqrt(k))+1): #최대 약수의 모든 약수 찾기
    if k%i == 0: 
        div.append(i)#k 나누어떨어지게 하는 수
        div.append(k//i) #i로 나눈 값

div=list(set(div))
div.sort()

for a in div:
    for i in range(N):
        if i==N-1:
            print(a, end=" ")
        elif num[i]%a!=num[i+1]%a: #나머지 같은지 확인
            break
        
