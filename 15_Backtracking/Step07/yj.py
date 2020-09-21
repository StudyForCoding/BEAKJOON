import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

minimum = 1e9
maximum = -1e9
def result(now, index):
    if index == N:
        global minimum, maximum
        maximum = max(now, maximum)
        minimum = min(now, minimum)
        return
    if operator[0] > 0:
        operator[0] -= 1
        result(now + numList[index], index+1)
        operator[0] += 1
    if operator[1] > 0:
        operator[1] -= 1
        result(now - numList[index], index+1)
        operator[1] += 1
    if operator[2] > 0:
        operator[2] -= 1
        result(now * numList[index], index+1)
        operator[2] += 1
    if operator[3] > 0:
        operator[3] -= 1
        result(int(now/ numList[index]), index+1)
        operator[3] += 1

now = numList[0]
result(now, 1)
print(maximum)
print(minimum)
