n = int(input())
count_2 = 0
count_5 = 0
for i in range(2,n+1):
    num = i
    while(1):
        if num%2 == 0: 
            count_2 += 1
            num //= 2 
        elif num%5 == 0: 
            count_5 += 1
            num //= 5
        else: break
print(min(count_2,count_5))