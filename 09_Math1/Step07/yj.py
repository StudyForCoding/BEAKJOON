T = int(input())
for a in range(T):
    
    people=0
    k = int(input())
    n = int(input())

    base =[]
    base.append([])
    for i in range(n) : 
        base[0].append(i+1)
    for floor in range(1,k+1):
        base.append([])
        for num in range(n):
            people = 0
            for nu in range(num+1):
                people += base[floor-1][nu]
            base[floor].append(people)
    print(base[-1][-1])
        