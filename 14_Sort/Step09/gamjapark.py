n = int(input())

people = []
for i in range(n):
	a, b = input().split()
	people.append((int(a), b, i))
people.sort(key=lambda x:(x[0], x[2]))

for p in people:
	print(p[0], p[1])