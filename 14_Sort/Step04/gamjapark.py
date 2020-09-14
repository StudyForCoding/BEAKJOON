import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

#산술평균
print(round(sum(arr) / N))


#중앙값
arr.sort()
if N % 2 == 0: #짝수
	print((arr[N//2] + arr[N//2 - 1]) / 2)
else:
	print(arr[(N//2)])


#최빈값
count = {}
for i in arr:
	try: count[i] += 1
	except: count[i] = 1
tmp = sorted(count.items(), reverse=True, key=lambda x:x[1])

if  len(arr) != 1 and tmp[0][1] == tmp[1][1]:
	print(tmp[1][0])
else:
	print(tmp[0][0])

#범위
min_val = min(arr)
max_val = max(arr)
print(max_val - min_val)