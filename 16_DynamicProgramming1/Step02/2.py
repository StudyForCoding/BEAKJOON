T=int(input()) #테스트케이스 개수
arr=[]#테스트 케이스 배열
count_0=0
count_1=0
 
for i in range(T):
    N=int(input())
    arr.append(N)
    
list=[0 for i in range(50)] #0이 아니면 이미 계산한 위치

def fibo(n):
    if(n==0):
        global count_0
        count_0=count_0+1 #0출력할 때 count_0 1씩 증가
        return 0
    elif(n==1):
        global count_1
        count_1=count_1+1 #1출력할 때 count_1 1씩 증가
        return 1
    elif(list[n]!=0):
        return list[n]
    else:
        list[n]= fibo(n-1)+fibo(n-2)
    return list[n]

for i in arr:
    fibo(i)
    print(count_0, count_1) #0과 1 출력한 횟수 출력
    count_0=0 #초기화
    count_1=0 #기초

