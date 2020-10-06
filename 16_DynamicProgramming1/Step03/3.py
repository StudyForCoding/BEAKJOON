N=int(input())

list=[0 for i in range(50)]

def fibo(n):
    if(n==1):
        return 1
    if(n==2):
        return 2 #1, 2, 3, 5, 8...으로 나가는 점화식 
    if(list[n]!=0):
        return list[n]
    list[n]= fibo(n-1)+fibo(n-2)
    return list[n]

print(fibo(N))
