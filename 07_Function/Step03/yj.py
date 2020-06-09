N = int(input())
num = 0

def number(i):
    if i <100 : 
        return 1
    else : 
        a = i//100 
        b =  (i%100)//10  
        c =  (i%100)%10
        if a-b ==b-c:
            return 1
        else: return 0

for i in range(1,N+1):
    num+=number(i)
print(num)