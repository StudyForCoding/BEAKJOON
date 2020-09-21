import sys
from itertools import combinations

n = int(sys.stdin.readline())
teams = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

people = list(range(n))
candidate = list(combinations(people, n//2))

gap = 1e9

for start in candidate:
    link = set(people)-set(start)
    start_sum, link_sum = 0, 0
    start_combi = list(combinations(start,2))
    link_combi = list(combinations(link,2))

    for x, y in start_combi:
        start_sum += teams[x][y]+teams[y][x]
    for x, y in link_combi:
        link_sum += teams[x][y]+teams[y][x]
    if gap>abs(start_sum-link_sum):
        gap = abs(start_sum-link_sum)

print(gap)
