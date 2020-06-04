s = input()
ans = len(s)
cro = ["c=", "c-", "d-", "lj", "nj", "s=", "z=", "dz="]
for c in cro:
    ans -= s.count(c)
print(ans)
