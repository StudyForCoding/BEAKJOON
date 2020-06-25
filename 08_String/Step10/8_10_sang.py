n = int(input())
ans = 0
for i in range(n):
    s = input()
    flag = True
    for c in range(26):
        al = chr(c + ord('a'))
        count = s.count(al)
        if al * count not in s:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
