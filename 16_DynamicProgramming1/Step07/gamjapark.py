import sys
n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1 or n == 2:
	print(sum(score))
else:
	answer = [score[0], score[0] + score[1], max(score[0] + score[2], score[1] + score[2])]
	for i in range(3, n):
		answer.append(max(answer[i - 3] + score[i - 1] + score[i], answer[i - 2] + score[i]))

	print(answer[n - 1])