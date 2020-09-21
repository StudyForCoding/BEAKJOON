N=int(input())
M=int(input())  #N, M 입력받음
 
check = [False]*(N+1) # check가 False면 안쓰인것, True면 쓰인 것
a = [0]*M   #M크기의 배열(수열 들어갈 배열)
 
def algo(k,inc, N, M): 
    if k == M:
        for i in range(M):
            print (a[i], end = ' ') #완성된 수열 출력
        print()
        return
    else:
        for i in range(inc, N+1): 
            if check[i]:
                continue
            check[i] = True #i 사용했다는 표시를 주고
            a[k] = i #i 사용
            algo(k+1,i+1,N, M)
            check[i] = False #한 줄 출력했으면 초기화
 

algo(0,1,N,M)

#1이 맨 앞에 있을 때 2~4 출력
#2가 맨 앞에 있을 때 inc를 1 더해서 3~4출력하도록 함
