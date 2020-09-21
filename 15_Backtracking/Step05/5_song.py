n=int(input()) #n 입력받음

col=[0]*(n+1) #열을 나타내는 배열
count=0

def queens(i,col): #행과 열배열 파라미터로 줌(가지치기)
    global count
    n=len(col)-1
    if(promising(i, col)):#i행이 유망하다면
        if(i==n):
            count+=1
        else:             #queens함수로 아래노드 탐색
            for j in range(1,n+1): 
                col[i+1]=j #i 다음행의 열을 j로 지정
                queens(i+1, col) #i다음 행의 어떤 열이 유망한지 탐색
        

def promising(i, col):
    k=1    #행렬 (1,1)부터 시작
    check=True
    while(k<i and check):
        if(col[i]==col[k] or abs(col[i]-col[k])==(i-k)):#같은 열인지, 대각선이면
            check=False #False
        k+=1
    return check

queens(0,col)
print(count)


