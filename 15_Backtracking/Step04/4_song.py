N=int(input())
M=int(input())  #N, M 입력받음
 
a = [0]*M   #M크기의 배열(수열 들어갈 배열)
 
def algo(k,inc, N, M): 
    if k == M:
        for i in range(M):
            print (a[i], end = ' ') #완성된 수열 출력
        print()
        return
    else:
        for i in range(inc, N+1): 
            a[k] = i #i 사용
            algo(k+1,i,N, M) #(1, 1), (2, 2)와 같은 값도 나올 수 있도록 i+1을 i로 바꿈
 

algo(0,1,N,M)

#1이 맨 앞에 있을 때 2~4 출력
#2가 맨 앞에 있을 때 inc를 1 더해서 3~4출력하도록 함

#n과m(2)번 코드에서 check관련 코드 제거
