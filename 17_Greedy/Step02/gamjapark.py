import sys
N = int(sys.stdin.readline())
time = []
for i in range(N):
	(s, f) = map(int, sys.stdin.readline().split())
	time.append((s, f))

time = sorted(time, key=lambda x :(x[1], x[0]))

s, f = time[0][0], time[0][1]
count = 1
for i in range(1, N):
	(new_s, new_f) = time[i]
	if new_s >= f:
		count += 1
		s, f = new_s, new_f
print(count)