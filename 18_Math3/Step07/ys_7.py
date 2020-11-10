N, K=map(int, input().split())

calup=1 #분자
for i in range(N, N-K, -1):
    calup*=i

caldown=1 #분모
for i in range(1, K+1):
    caldown*=i

print(calup//caldown)
