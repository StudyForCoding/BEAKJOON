import sys

N = sys.stdin.readline().rstrip().split('-')
num = []
for i in N:
    if '+' in i:
        new = map(int, i.split('+'))
        num.append(sum(new))
    else:
        num.append(int(i))

print(num[0]-sum(num[1:]))