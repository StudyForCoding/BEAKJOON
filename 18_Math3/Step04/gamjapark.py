import sys
x, y = map(int, sys.stdin.readline().split())

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def lcm(a, b):
	return (a * b) // gcd(a, b)

print(gcd(x, y))
print(lcm(x, y))