import sys
T = int(sys.stdin.readline())

for i in range(T):
	N = int(sys.stdin.readline())
	cloth_dict = dict()
	for j in range(N):
		name, kind = sys.stdin.readline().split()
		try:
			cloth_dict[kind] += 1
		except:
			cloth_dict[kind] = 2
	
	answer = 1
	for c in list(cloth_dict.values()):
		answer *= c
	print(answer - 1)