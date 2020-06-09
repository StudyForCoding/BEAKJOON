def isArithmeticProgression(n):
    num_list = list(map(int, list(str(n))))
    if len(num_list) == 1:
        return True
    d = num_list[1] - num_list[0]
    for i in range(2,len(num_list)):
        if d != (num_list[i] - num_list[i-1]):
            return False
    return True
N=int(input())

count=0
for i in range(1, N + 1):
    if isArithmeticProgression(i):
        count+=1
print(count)
