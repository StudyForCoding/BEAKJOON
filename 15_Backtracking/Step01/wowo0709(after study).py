def find(n,m,index):
  if index == m:
    print(" ".join(map(str,foundlist)))
    return 
  else:
    for i in range(1,n+1):
      if findnum[i] == True:
        continue
      else:
        findnum[i] = True
        foundlist[index] = i
        find(n,m,index+1)
        findnum[i] = False

n,m = map(int,input().split())
findnum = [False]*(n+1)
foundlist = [0]*m
find(n,m,0)