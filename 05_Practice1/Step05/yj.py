a = int(input())
for i in range(a):
    print(' '*i+'*'*(a-i)+'*'*(a-i-1))
for i in range(1,a):
    print(' '*(a-i-1)+'*'*(i)+'*'*(i+1))