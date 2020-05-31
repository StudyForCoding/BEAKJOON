n = int(input())
for i in range(n):
    if n % 2 == 0: #짝수
        for j in range(n - 1):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        for j in range(n):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    else: #홀수
        for j in range(n):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        for j in range(n - 1):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()