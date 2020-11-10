import math
n = int(input())
num = [] #수를 담아놓는 용도의 리스트
# 중복을 없애기 위해 set으로 선언
ans = set()
gcd = 0
for i in range(n):
    num.append(int(input()))
    #'앞 숫자와의 차'와 '앞 숫자까지의 gcd' 사이의 gcd를 구한다. 
    if i == 1:
        gcd = abs(num[1]-num[0])
    gcd = math.gcd(abs(num[i]-num[i-1]),gcd)
    # gcd의 약수 구하기
for i in range(1,int(gcd**0.5)+1):
    if gcd % i == 0:
        ans.add(i)
        ans.add(gcd//i)
for a in sorted(list(ans - {1})): #1은 제외
    print(a,end=' ')