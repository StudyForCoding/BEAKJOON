n = int(input())
for i in range(n):
    H, W, N = map(int, input().split())
    answer = ""
    if N % H == 0:
        floor = H
        room = N // H
    else:
        floor = N % H
        room = (N // H) + 1

    answer += str(floor)
    if len(str(room)) == 1:
        answer += "0"
    answer += str(room)
    print(answer)