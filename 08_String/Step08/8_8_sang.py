s = input()
a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
ans = 0
for c in s:
    for i, al in enumerate(a):
        if c in al:
            ans += 3 + i
print(ans)
