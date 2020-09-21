'''1. 연산자 배치해서 각 값 계산
   1-1. 연산자 하나골라서 연산, 거기에 또 연산자 골라서 연산(연산함수로 반복)
   2. 최대값, 최소값 구해서 출력'''
#https://claude-u.tistory.com/371 참고
N=int(input()) #순열의 개수
p=list(map(int, input().split()))#순열배열
add, sub, mul, div = map(int, input().split()) #연산자 개수
min1, max1= 1e9, -1e9 #최대, 최소값 초기화

def operation(i, initial, add, sub, mul, div):
    global max1, min1
    if i==N:
        max1=max(initial,max1) #전 줄의 값과 비교-> 최대값 저장
        min1=min(initial,min1) #전 줄의 값과 비교-> 최소값 저장
        return
    else:
        if add:
            operation(i+1, initial+p[i], add-1, sub, mul, div) #+연산해서 operation함수로
        if sub:
            operation(i+1, initial-p[i], add, sub-1, mul, div) #-연산해서 operation함수로
        if mul:
            operation(i+1, initial*p[i], add, sub, mul-1, div) #*연산해서 operation함수로
        if div:
            operation(i+1, int(initial/p[i]), add, sub, mul, div-1) #/연산해서 operation함수로
            
operation(1, p[0], add, sub, mul, div)
print(max1)
print(min1)
    
    

    

