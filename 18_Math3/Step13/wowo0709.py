import sys
input = sys.stdin.readline
import math

test = int(input())
for t in range(test):
    n,m = map(int,input().split())
    print(math.factorial(m)//(math.factorial(m-n)*math.factorial(n)))