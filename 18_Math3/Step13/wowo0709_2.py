import sys
input = sys.stdin.readline
from functools import reduce

def nCm(n,m):
    m = min(m,n-m)

    numerator = reduce(lambda x,y:x*y,range(n,n-m,-1),1)
    denominator = reduce(lambda x,y:x*y,range(m,1,-1),1)
    return numerator // denominator

test = int(input())
for t in range(test):
    n,m = map(int,input().split())
    print(nCm(m,n))