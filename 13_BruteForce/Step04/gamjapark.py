a, b = map(int, input().split())
temp = []
for i in range(a):
    temp.append(input())

def map8by8(start, map):
    count = 0
    check = start
    for i in range(8):
        for j in range(8):
            if map[i][j] != check:
                count += 1
            if j != 7 and check == 'W':
                check = 'B'
            elif j != 7 and check == 'B':
                check = 'W'
    return count

result = []
for i in range(a - 7):
    for j in range(b - 7):
        map = []
        for k in range(i, i + 8):
            map.append(list(temp[k][j:j + 8]))
        result.append(map8by8('W', map))
        result.append(map8by8('B', map))

print(min(result))