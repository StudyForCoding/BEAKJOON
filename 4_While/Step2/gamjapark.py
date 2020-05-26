import sys
for line in sys.stdin:
    if line == "":
        break
    a, b = map(int, line.split())
    print(a+b)