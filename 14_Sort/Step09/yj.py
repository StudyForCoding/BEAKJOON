import sys
N = int(sys.stdin.readline())
people=[]
for i in range(N):
    old, name = sys.stdin.readline().rstrip().split()
    people.append((int(old),name))
people.sort(key=lambda people:people[0])

for person in people:
    print(person[0],person[1])