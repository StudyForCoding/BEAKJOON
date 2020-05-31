import sys
product = 1
for i in range(3):
    x = sys.stdin.readline().rstrip()
    product = product * int(x)
arr = list(str(product))
for i in range(10):
    print(arr.count(str(i)))