N=int(input()) #정수

c = [0]*(N+1)
c[0]=0
c[1]=0

for i in range(2,N+1):
    if (i%3 == 0 and i%2 == 0): #2와 3으로 모두 나누어떨어질 경우
      c[i] = min(c[i//3], c[i//2], c[i-1]) + 1 
      continue    
    elif (i%3 == 0 and i%2 != 0): #3으로 나누어지고 2로 나누어지지 않을 경우
      c[i] = min(c[i//3], c[i-1]) + 1
      continue
    elif (i%3 != 0 and i%2 == 0): #3으로 나누어지지 않고 2로 나누어질 경우
      c[i] = min(c[i//2], c[i-1]) + 1
      continue
    else: #2와 3으로 모두 나누어떨어지지 않을 경우
      c[i] = c[i-1] + 1

print(c[N])

