N = dict()
for i in range(1,10):
    N[int(input())]=i
print(max(N.keys()))
print(N.get(max(N.keys())))