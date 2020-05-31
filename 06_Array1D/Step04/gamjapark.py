import sys
arr = []
for i in range(10):
    x = sys.stdin.readline().rstrip()
    arr.append(int(x)%42)
arr = list(set(arr))
print(len(arr))