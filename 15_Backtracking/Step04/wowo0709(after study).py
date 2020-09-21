def find(n,m,index,cursor):
  if index == m:
    print(" ".join(map(str,foundlist)))
    return 
  else:
    for i in range(cursor,n+1):
      foundlist[index] = cursor = i
      find(n,m,index+1,cursor)

n,m = map(int,input().split())
foundlist = [0]*m
find(n,m,0,1)