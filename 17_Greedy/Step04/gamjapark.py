import sys
aa = sys.stdin.readline().strip()
one = aa.split('-')
answer = sum(map(int, one[0].split('+')))

for i in range(1, len(one)):
	answer -= sum(map(int, one[i].split('+')))
print(answer)