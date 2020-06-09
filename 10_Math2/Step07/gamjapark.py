x_ = []
y_ = []
cor = []
for i in range(3):
    x, y = map(int, input().split())
    x_.append(x)
    y_.append(y)
    cor.append([x,y])

x_1 = list(set(x_))
y_1 = list(set(y_))
x_1.sort()
y_1.sort()

min_x = x_1[0]
min_y = y_1[0]

w = x_1[1] - x_1[0]
h = y_1[1] - y_1[0]

if not [min_x, min_y] in cor:
    print("%d %d"%(min_x, min_y))
elif not [min_x + w, min_y] in cor:
    print("%d %d"%(min_x + w, min_y))
elif not [min_x, min_y + h] in cor:
    print("%d %d"%(min_x, min_y +h))
elif not [min_x+w, min_y+h] in cor:
    print("%d %d"%(min_x +w, min_y+h))