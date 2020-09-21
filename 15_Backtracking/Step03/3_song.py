N=int(input())
M=int(input())  #N, M 입력받음
 
a = [0]*M   #M크기의 배열(수열 들어갈 배열)
 
def algo(k, N, M):
    if k == M:       
        for i in range(M):
            print (a[i], end = ' ') #완성된 수열 출력
        print()
        return
    else:
        for i in range(1, N+1):
            a[k] = i #i 사용
            algo(k+1, N, M)
 
algo(0,N,M)
    
#중복을 방지하기 위한 배열인 check관련 코드 모두 제거
