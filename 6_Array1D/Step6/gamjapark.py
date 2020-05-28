import sys
n=int(input())
for i in range(n):
    arr = list(str(sys.stdin.readline().rstrip()))
    count = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            count += 1
            arr[j] = count
        elif arr[j] == 'X':
            count = 0
            arr[j] = 0
    print(sum(arr))