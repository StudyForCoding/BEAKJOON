T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    for s in S:
        print(s*R, end="")
    print()