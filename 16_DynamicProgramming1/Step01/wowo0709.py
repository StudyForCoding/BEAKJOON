n = int(input())
fibo_num = [0,1]
for i in range(2,n+1):
  fibo_num.append(fibo_num[i-1]+fibo_num[i-2])
print(fibo_num[n])