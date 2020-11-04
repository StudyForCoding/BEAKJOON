n = int(input())
p = list(map(int,input().split()))
p.sort()
sum_ = 0
for i in range(len(p)+1):
    sum_ += sum(p[:i])
print(sum_)