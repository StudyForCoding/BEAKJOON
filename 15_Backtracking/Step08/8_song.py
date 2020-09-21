'''1. N명 중 N/2명 뽑기(순서상관x-> 조합)
   2. 각 팀의 능력치 합 계산
   3. 두 팀의 능력치 차이 계산
   4. 두 팀의 능력치 차이 최소값 출력'''
#https://juhee-maeng.tistory.com/60 참고
import sys #능력치 지도 입력받기 위해
import math #조합함수 쓰기위해
from itertools import combinations
N=int(input())
result=math.inf #result 무한대로 놓음
map1=[]
for _ in range(N): #능력치 지도 입력받기
    map1.append(list(map(int,sys.stdin.readline().split())))

people=list(range(N))
team1=list(combinations(people,N//2))

for team in team1:
    team2=list(set(people)-set(team)) #team2 지정
    team_sum, team2_sum=0, 0 #팀 능력치 초기화
    team_combi=list(combinations(list(team),2)) #team1 두명식 묶어줌
    team2_combi=list(combinations(list(team2),2)) #team2 두명식 묶어줌

    for i, j in team_combi:
        team_sum+=(map1[i][j]+map1[j][i]) #team1 능력치 합

    for i, j in team2_combi:
        team2_sum+=(map1[i][j]+map1[j][i]) #team2 능력치 합

    if result>abs(team_sum-team2_sum): #result의 최소값 찾기
        result=abs(team_sum-team2_sum)

print(result)
           
           
