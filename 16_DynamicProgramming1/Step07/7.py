import sys
N=int(input()) #계단 개수

stair = [0]*301 #계단 점수배열

for i in range(1, N+1):
    stair[i]=int(sys.stdin.readline())

dp=[0]*301 #점수 합 배열
dp[1]=stair[1] #N이 1일때 
dp[2]=stair[1]+stair[2] #N이 2일때
dp[3]=max(stair[3]+stair[1],stair[3]+stair[2]) #N이 3일때

for i in range(4, N+1):
    dp[i]=max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3]) #N이 3 이상일 때

print(dp[N]) #점수 최대값 출력
