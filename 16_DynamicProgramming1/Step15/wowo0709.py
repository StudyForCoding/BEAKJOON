import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
dp = [0]*n;dp[0] = nums[0]
for i in range(1,n):
    dp[i] = max(nums[i],nums[i]+dp[i-1])
print(max(dp))