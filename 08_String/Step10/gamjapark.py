n = int(input())
count = 0
for i in range(n):
    one_word = list(input())
    count_arr = [0 for _ in range(26)]
    pre = ""
    for c in one_word:
        idx = ord(c) - 97
        cur = c
        if (count_arr[idx] == 0) or (pre == cur):
            count_arr[idx] += 1
        pre = c
    if sum(count_arr) == len(one_word):
        count += 1
print(count)