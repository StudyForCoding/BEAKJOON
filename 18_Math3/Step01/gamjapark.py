import sys
def isFactor(a, b):
	return (b % a == 0)
def isMultiple(a, b):
	return (a % b == 0)
while True:
	x, y = map(int, sys.stdin.readline().split())
	if x == 0 and y == 0:
		break
	if isFactor(x, y) and not isMultiple(x, y):
		print('factor')
	elif not isFactor(x, y) and isMultiple(x, y):
		print('multiple')
	elif not isFactor(x, y) and not isMultiple(x, y):
		print('neither')