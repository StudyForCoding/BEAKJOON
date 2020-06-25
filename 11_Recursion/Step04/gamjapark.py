def hanoi(n, pos, r, des):
    if n == 1:
        print("%d %d"%(pos, des))
        return

    hanoi(n - 1, pos, des, r)
    print("%d %d"%(pos, des))
    hanoi(n - 1, r, pos, des)

n = int(input())
print((2**n) - 1)
hanoi(n, 1,2,3)