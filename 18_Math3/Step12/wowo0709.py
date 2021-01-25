'''유클리드 호제법'''
import sys
input = sys.stdin.readline

def GCD(a,b):
    if(a%b == 0):  return b
    return GCD(b,a%b)

test = int(input())
for t in range(test):
    a,b = map(int,input().split())
    print(a*b//GCD(a,b))