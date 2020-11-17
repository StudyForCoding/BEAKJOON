import sys

while True:
	ss = sys.stdin.readline().rstrip()
	if ss == '.':
		break
	ps = []
	for s in ss:
		if s == '(' or s == '[':
			ps.append(s)
		elif s == ']':
			if not ps or ps.pop() != '[':
				ps.append(s)
				break
		elif s == ')':
			if not ps or ps.pop() != '(':
				ps.append(s)
				break
	if not ps:
		print('yes')
	else:
		print('no')
