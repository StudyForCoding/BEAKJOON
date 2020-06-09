import sys
a = int(input())
for i in range(a):
    c,d = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1,c,d,c+d))