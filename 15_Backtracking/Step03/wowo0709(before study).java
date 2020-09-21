import sys
N,M = map(int,sys.stdin.readline().split())
array = [1]*M

while(1):
  if N+1 in array: #N+1인 수가 존재할 때
    index = array.index(N+1)
    if index == 0: # N+1인 수가 첫번째 수 일때
      sys.exit()
    else: # N+1인 수가 첫번째 수가 아닐 때
      array[index-1] += 1
      for i in range(index,M):
        array[i] = 1
  else: # N+1인 수가 없을 때
    for element in array:  
      sys.stdout.write(str(element)+' ')
    sys.stdout.write('\n')
    array[len(array)-1] += 1