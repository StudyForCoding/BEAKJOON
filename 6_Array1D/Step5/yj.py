N = int(input())
score = list(map(int, input().split()))
M=max(score)
new_avg= sum(score)/M*100/N
print(new_avg)