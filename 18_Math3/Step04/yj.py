import sys
from math import gcd

N, M = map(int, sys.stdin.readline().split())
print(gcd(N,M))
print(N*M//gcd(N,M))