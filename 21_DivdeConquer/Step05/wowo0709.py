'''
다이나믹 프로그래밍의 풀이로 접근하면 시간초과가 난다. 이 문제는 입력되는 수의 크기가 매우 크기 때문에
'페르마의 소정리'를 이용해야 한다. => a^(p-1) = 1(mod p) // p는 소수이고 a는 p로 나누어지지 않는 정수
이항 계수: (n!/(k!(n-k)!)) % p = [{n! % p} * {(k!(n-k)!)^p-2 % p}] % p
결과적인 시간복잡도는 O(N + logN)
'''
import sys
input = sys.stdin.readline
## 백준 1629번에서 풀이한 거듭제곱 구하기 함수 활용
def find_power(number,power):
    if power == 0:
        return 1
    if power == 1:
        return number
    
    if power % 2 == 0:
        return find_power(number,power//2) ** 2 % div
    else:
        return find_power(number,power-1) * number % div

n,k = map(int,input().rstrip().split())

numerator,denominator,div = 1,1,int(1e+9 + 7)
# STEP 1. 페르마의 정리에 따라 얻은 이항계수 변환식의 n!, k!, (n-k)! 구하기
for i in range(2,n+1):
    numerator *= i
    numerator %= div
for j in range(2,k+1):
    denominator *= j
    denominator %= div
for k in range(2,n-k+1):
    denominator *= k
    denominator %= div
# STEP 2. 분모의 (p-2) 제곱 구하기
denominator = find_power(denominator,div-2)
# STEP 3. 최종적으로 답 구하기
print(numerator*denominator%div)