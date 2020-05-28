min1 = int(input())
for i in range(2):
    a = int(input())
    if a < min1:
        min1 = a
cola = int(input())
sydar = int(input())
min2 = cola if cola < sydar else sydar
print(min1 + min2 - 50)