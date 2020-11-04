import sys
N =int(sys.stdin.readline())

meeting = []
for i in range(N):
    meeting.append(list(map(int,sys.stdin.readline().split())))
meeting.sort(key=lambda x:(x[1],x[0]))

num =0
last = 0
for j in meeting:
    if last<=j[0]:
        num+=1
        last = j[1]
print(num)