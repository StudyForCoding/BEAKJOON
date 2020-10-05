import sys
n = int(input())
pricelist = [[int(price) for price in sys.stdin.readline().split()] for home in range(n)]
for i in range(1,n):
    pricelist[i][0] += min(pricelist[i-1][1],pricelist[i-1][2])
    pricelist[i][1] += min(pricelist[i-1][0],pricelist[i-1][2])
    pricelist[i][2] += min(pricelist[i-1][0],pricelist[i-1][1])
print(min(pricelist[n-1]))