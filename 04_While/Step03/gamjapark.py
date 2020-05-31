n = int(input())
temp_n = n
k=0
while True:
    a = int(temp_n / 10)
    b = temp_n % 10
    c = (a + b) % 10
    new = b*10 + c
    k += 1
    if new == n:
        break
    temp_n = new
print(k)
