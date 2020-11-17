import sys
T = int(sys.stdin.readline())
for i in range(T):
	pString = sys.stdin.readline()
	ps = []
	for p in pString:
		if p == '(':
			ps.append(p)
		elif p == ')':
			if not ps:
				ps.append(p)
				break
			else:
				ps.pop()
	if not ps:
		print('YES')
	else:
		print('NO')