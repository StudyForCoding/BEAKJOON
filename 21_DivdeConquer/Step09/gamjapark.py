import sys

high = []

def solution(start, end):
	if start == end:
		return high[start]
	else:
		# 왼쪽이랑 오른쪽 중 가장 큰 것
		mid = (start + end) // 2
		max_lr_high = max(solution(start, mid), solution(mid + 1, end))
		
		# 경계선
		cur_height = min(high[mid], high[mid + 1])
		cur_width = 2
		hori_area = max(max_lr_high, cur_width * cur_height)

		left, right = mid, mid + 1
		while start < left or right < end:
			cur_width += 1
			if start < left and right < end:
				if high[right + 1] > high[left - 1]:
					cur_height = min(cur_height, high[right + 1])
					right += 1
				else:
					cur_height = min(cur_height, high[left - 1])
					left -= 1
			elif start < left:
				cur_height = min(cur_height, high[left - 1])
				left -= 1
			else:
				cur_height = min(cur_height, high[right + 1])
				right += 1

			hori_area = max(hori_area, cur_width * cur_height)
		return hori_area

while True:
	high = list(map(int, sys.stdin.readline().split()))
	if high[0] == 0:
		break
	N = high[0]
	high = high[1:N+1]
	print(solution(0, N-1))

	