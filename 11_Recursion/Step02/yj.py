def pibo(n):
    if n==0: return 0
    if n==1: return 1
    else: return pibo(n-2)+pibo(n-1)
print(pibo(int(input())))