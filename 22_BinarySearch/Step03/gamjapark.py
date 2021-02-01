#108ms

import sys
K, N = map(int, sys.stdin.readline().split())
lanLength = [int(sys.stdin.readline()) for i in range(K)]

minLen = 1
maxLen = max(lanLength)

while minLen <= maxLen:
	mid = (maxLen + minLen) // 2
	sumCount = 0
	for l in lanLength:
		sumCount += (l // mid)

	if sumCount >= N:
		minLen = mid + 1
	else:
		maxLen = mid - 1
print(maxLen)
	