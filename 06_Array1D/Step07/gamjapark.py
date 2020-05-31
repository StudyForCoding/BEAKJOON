import sys
c = int(input())
for i in range(c):
    arr = sys.stdin.readline().rstrip().split()
    n = int(arr[0])
    del arr[0]
    arr = list(map(int, arr))
    ave = sum(arr)/n
    count = 0
    for k in arr:
        if k > ave:
            count += 1
    print("%0.3f%%"%(count/n*100))
	