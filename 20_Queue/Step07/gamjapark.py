import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
	action = sys.stdin.readline().split()[0]
	n = int(sys.stdin.readline())
	arr = sys.stdin.readline().splitlines()[0].lstrip("[")
	arr = arr.rstrip("]")
	if n != 0:
		arr = deque(map(int,arr.split(",")))
	else:
		arr = deque()
	check = 0
	pop_check = "left"
	for a in action:
		if a == "R":
			if pop_check == "left":
				pop_check = "right"
			elif pop_check == "right":
				pop_check = "left"
		elif a == "D":
			if len(arr) == 0:
				check = 1
				break
			if pop_check == "left":
				arr.popleft()
			elif pop_check == "right":
				arr.pop()
	if check:
		print("error")
	else:
		if pop_check == "right":
			arr.reverse()
		
		print("[", end="")
		for i in range(len(arr)):
			if i == len(arr) - 1:
				print(arr[i], end="")
			else:
				print(str(arr[i]) + ",", end="")
		print("]")