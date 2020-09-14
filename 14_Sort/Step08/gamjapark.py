n = int(input())
pos_dict = {}
for i in range(n):
	s = input()
	pos_dict[s]=len(s)
pos = []
for k, v in pos_dict.items():
	pos.append((k, v))
pos.sort(key=lambda x:(x[1], x[0][:]))
for p in pos:
	print(p[0])