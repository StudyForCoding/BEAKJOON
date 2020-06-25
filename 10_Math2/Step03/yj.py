import sys
import math
M,N = map(int,sys.stdin.readline().split())

def primenum(i):
    if i ==1: return 0
    for a in range(2,int(math.sqrt(i))+1):
        if i%a==0:
            return 0
    return 1

for i in range(M,N+1):
    if primenum(i)==1: print(i) 