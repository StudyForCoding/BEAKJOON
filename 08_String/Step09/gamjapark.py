words = input()
croatias = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
count = 0
while True:
    check = True
    for croatia in croatias:
        if words[i:i + len(croatia)] == croatia:
            i = i + len(croatia)
            check = False
            break
    if check:
        i += 1
    count += 1
    if i == len(words):
        break

print(count)