T=int(input()) #테스트케이스 개수
arr=[]#테스트 케이스 배열
 
for i in range(T):
    N=int(input())
    arr.append(N)
    
list=[0 for i in range(50)] #0이 아니면 이미 계산한 위치

def pado(n):
    if(n==1): #세번째까지 초기화되어있기 때문에 0번째 필요x
        return 1
    elif(n==2):
        return 1
    elif(n==3): 
        return 1
    elif(list[n]!=0):
        return list[n]
    else:
        list[n]= pado(n-2)+pado(n-3)
    return list[n]

for i in arr:
    print(pado(i))


