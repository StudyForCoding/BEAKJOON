X = int(input())
n=1
while (X>n): 
    X-=n
    n+=1
if n%2==1:
    print('%d/%d'%(n+1-X,X)) 
else : 
    print('%d/%d'%(X,n+1-X))
        