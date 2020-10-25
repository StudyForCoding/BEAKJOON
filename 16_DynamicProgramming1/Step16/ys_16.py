N, K = map(int, input().split(' '))
map1 = [ [0]*(K+1) for i in range(N+1) ]
#map1[i][j]=배낭에 넣은 물품 무게 합이 j일때 최대가치

for i in range(1, N+1):
    w, v = map(int, input().split(' '))
    for j in range(1, K+1):
        if j < w: #j가 w보다 작으면 가방에 담을 수 없음
            map1[i][j] = map1[i-1][j] #과거의 값 그대로 복사
        else:
            #w의 가치과 v를 거해준 값과 j의 이전값과 비교해서 최대
            map1[i][j] = max(map1[i-1][j], map1[i-1][j-w] + v)
            
            
print(map1[N][K])
