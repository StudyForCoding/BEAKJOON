n = int(input())
count = 0
column,rightup,rightdown = [False]*n,[False]*(2*n-1),[False]*(2*n-1)

def NQueen(line):
  global count
  if line == n:
    count += 1
    return
  else:
    for index in range(n):
      if not (column[index] or rightup[line+index] or rightdown[line-index+n-1]):
        column[index] = rightup[line+index] = rightdown[line-index+n-1] = True
        NQueen(line+1)
        column[index] = rightup[line+index] = rightdown[line-index+n-1] = False

NQueen(0)
print(count)