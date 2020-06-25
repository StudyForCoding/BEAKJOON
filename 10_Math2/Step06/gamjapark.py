x, y, w, h = map(int, input().split())
min_list = [x, w - x, y, h - y]
print(min(min_list))