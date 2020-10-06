N=int(input()) #계단 개수

stair = [] #계단 점수배열

for i in range(N):
    stair.append(int(input()))

sum=[] #점수 합 배열
sum.append(stair[0]) #N이 1일때 
sum.append(stair[1]+stair[0]) #N이 2일때
sum.append(max(stair[2]+stair[0],stair[2]+stair[1])) #N이 3일때

for i in range(3, N):
    sum.append(max(stair[i]+sum[i-2], stair[i]+stair[i-1]+sum[i-3])) #N이 3 이상일 때

print(sum[N-1]) #점수 최대값 출력
