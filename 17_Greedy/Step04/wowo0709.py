eq=list(input().split('-'))
sumlist = []
for i in range(len(eq)):
    sumlist.append(sum(list(map(int,eq[i].split('+')))))
print(sumlist[0]-sum(sumlist[1:]))