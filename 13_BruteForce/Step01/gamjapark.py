N, M = map(int, input().split())
nums = list(map(int, input().split()))

from itertools import combinations
nums_c = list(combinations(nums, 3))
answer = 0
for num in nums_c:
    sum1 = sum(num)
    if sum1 <= M and sum1 > answer:
        answer = sum1
print(answer)