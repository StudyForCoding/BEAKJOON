import sys
num = int(sys.stdin.readline())

if num == 0 or num == 1:
	print(num)
else:
	temp1, temp2, answer = 0, 1, 0

	for i in range(2, num + 1):
		answer = temp1 + temp2
		temp1 = temp2
		temp2 = answer
	print(answer)