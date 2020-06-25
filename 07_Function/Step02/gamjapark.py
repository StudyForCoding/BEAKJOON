def d(n):
    return n + sum(list(map(int, list(str(n)))))

nums = [x for x in range(1, 10001)]
for i in range(1, 10001):
    if d(i) in nums:
        nums.remove(d(i))
for num in nums:
    print(num)