import sys
input = sys.stdin.readline

n = int(input())
command = []
top = -1
stack = [0]*10000
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        top += 1
        stack[top] = int(command[1])
    elif command[0] == 'pop':
        if top != -1:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(top+1)
    elif command[0] == 'empty':
        print(int(top==-1))
    elif command[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])