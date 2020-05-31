t = int(input())
for i in range(t):
    count = 0
    score = 0
    s = input()
    for j in s:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
