
N = int(input()) #수열길이
arr = [*map(int, input().split())] #수열
inc = [0] * N #수열 증가부분
dec = [0] * N #수열 감소부분
cnt = 0

for i in range(N): #증가부분
    inc[i] = 1
    for j in range(i):
        if arr[j] < arr[i] :
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N - 1, -1, -1): #감소부분
    dec[i] = 1
    for j in range(N - 1, i -1, -1):
        if arr[j] < arr[i] :
            dec[i] = max(dec[i], dec[j] + 1)

for i in range(N):
    if cnt < inc[i] + dec[i] - 1:
        cnt = inc[i] + dec[i] - 1 #가장 긴 수열의 길

print(cnt)
