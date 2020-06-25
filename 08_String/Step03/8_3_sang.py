s = input()
al = [-1 for i in range(26)]
for i, c in enumerate(s):
    n = ord(c) - ord('a')
    if al[n] == -1:
        al[n] = i
for i in al:
    print(i, end=" ")
