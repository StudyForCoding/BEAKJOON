import sys
N = int(input())
point = []
for i in range(N):
  point.append(list(map(int,sys.stdin.readline().split())))

point.sort(key = lambda p:(p[1],p[0]))
for p in point:
  sys.stdout.write(str(p[0])+" "+str(p[1])+"\n")