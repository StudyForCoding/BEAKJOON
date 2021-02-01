import sys
input = sys.stdin.readline
    
def find_power(number,power):
    if power == 0:
        return 1
    if power == 1:
        return number % denominator
    
    if power % 2 == 0:
        return find_power(number,power//2) ** 2 % denominator
    else:
        return find_power(number,power-1) * number % denominator

number, power, denominator = map(int,input().rstrip().split())
answer = find_power(number,power)
print(answer)

## 제출 답안에서 나머지를 요구할 경우 앞의 계산 과정에서 미리 나머지를 구해서 메모리 사용량을 줄인다. 
## 재귀함수를 여러번 호출하지 않고 한 번 호출의 결과를 변수에 저장해 사용해서 함수 호출의 횟수를 줄인다. 