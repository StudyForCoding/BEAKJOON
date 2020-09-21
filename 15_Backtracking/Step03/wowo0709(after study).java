def find(n,m,index):
  if index == m:
    print(" ".join(map(str,foundlist)))
    return 
  else:
    for i in range(1,n+1):
      foundlist[index] = i
      find(n,m,index+1)

n,m = map(int,input().split())
foundlist = [0]*m
find(n,m,0)