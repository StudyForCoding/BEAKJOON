'''1. 스도쿠에서 0이 있는 곳을 찾음
   2. 해당 칸에 들어갈 수 있는 숫자 찾음(유망성 검사)
   2-1. 유망성검사: 행, 열, 3x3박스 검사
   3. 유망한 숫자들을 집어넣는다.
   4. 다음 0인부분으로 넘어간다(재귀함수 호출)
   5. 재귀함수 호출해서 답이 없다면 그부분 다시 0으로 초기화
   6. 마지막 0까지 모두 넣으면 출력'''
#https://claude-u.tistory.com/360 참고 

sudoku=[list(map(int, input().split()))for _ in range(9)] #입력된 스도쿠 받음
zeros=[(i,j) for i in range(9) for j in range(9) if sudoku[i][j]==0] #0인 칸 찾아서 행렬 (i, j) 위치 저장

def promising(i, j):
    pro = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in pro:      #행 검사
            pro.remove(sudoku[i][k]) #행에 이미 있는 숫자 pro에서 제거
        if sudoku[k][j] in pro:      #열 검사
            pro.remove(sudoku[k][j]) #열에 이미 있는 숫자 pro에서 제거
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in pro: 
                pro.remove(sudoku[p][q])
    
    return pro #가능한 숫자 출력

flag = False #답이 출력되었는가?

def main(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row) #리스트 요소  출력
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x] #0의 행렬위치가 i, j가 됨
        pro = promising(i, j) #유망한 숫자들을 받음
        
        for num in pro:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            main(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)

dfs(0)
