N = int(input())

check = False
for i in range(1, N):
    nums = list(map(int, str(i)))
    sum1 = i + sum(nums)
    if sum1 == N:
        print(i)
        check = True
        break

if not check:
    print(0)
