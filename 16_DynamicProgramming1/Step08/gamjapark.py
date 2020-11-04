import sys
N = int(sys.stdin.readline())

answer = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        answer[i] = 0
        continue
    answer[i] = answer[i - 1] + 1
    if i % 3 == 0 and answer[i // 3] + 1 < answer[i]:
        answer[i] = answer[i//3] + 1
    if i % 2 == 0 and answer[i // 2] + 1< answer[i]:
        answer[i] = answer[i // 2] + 1
        
print(answer[N])