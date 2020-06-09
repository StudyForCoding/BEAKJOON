A, B, V = map(int, input().split())
a = V - A
one_day = A - B
n = ((a // one_day) if a % one_day == 0 else ((a // one_day) + 1))
print(n + 1)