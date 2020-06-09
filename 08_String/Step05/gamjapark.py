s = list(input().upper())
count={}
for i in s:
    try: count[i] += 1
    except: count[i] = 1
count_list = list(count.values())
max_value = max(count.keys(), key=lambda x:count[x])
print("?") if count_list.count(count[max_value]) > 1 else print(max_value)
