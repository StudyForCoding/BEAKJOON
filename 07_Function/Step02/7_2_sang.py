l = [0 for i in range(10000)]
def selfnum(n):
    ans = n
    for i in str(n):
        ans += int(i)
    if ans <= 10000:
        l[ans - 1] = 1
        selfnum(ans)

for i in range(1, 10001):
    if l[i - 1] == 0:
        print(i)
        selfnum(i)
