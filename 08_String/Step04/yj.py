T = int(input())
for i in range(T):
    R, S=input().split()
    output = ''
    for i in S:
        output += i*int(R)
    print(output)