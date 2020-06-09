nums = list(map(int, list(input().split())))
print(-1) if (nums[2] - nums[1]) <= 0 else print(str(int(nums[0] / (nums[2] - nums[1])) + 1))