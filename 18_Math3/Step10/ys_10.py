N = int(input())
factorial = 1
count = 0
for i in range(1, N+1): #팩토리얼 계산
    factorial = factorial*i
    
while(factorial % 10 == 0):
    factorial = factorial//10
    count += 1
print(count)
