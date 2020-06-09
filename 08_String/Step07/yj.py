a, b = map(str,input().split())
print(max(''.join(reversed(a)),''.join(reversed(b))))