s = input().upper()
a, m = '', 0

for c in range(26):
    al = chr(c + ord('A'))
    print(al)
    if s.count(al) == 0:
        continue
    if m < s.count(al) and a != al:
        a = al
        m = s.count(al)
    elif a != c and m == s.count(al):
        a = '?'
print(a)
