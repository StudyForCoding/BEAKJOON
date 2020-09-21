def find(n,m,index,cursor):
  if index == m:
    print(" ".join(map(str,foundlist)))
    return 
  else:
    for i in range(cursor,n+1):
      if findnum[i] == True:
        continue
      else:
        findnum[i] = True
        foundlist[index] = cursor = i
        find(n,m,index+1,cursor)
        findnum[i] = False

n,m = map(int,input().split())
findnum = [False]*(n+1)
foundlist = [0]*m
find(n,m,0,1)