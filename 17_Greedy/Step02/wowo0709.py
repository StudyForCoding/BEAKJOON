n = int(input())
class_ = []
for i in range(n):
    start,end = input().split()
    class_.append([int(start),int(end)])
class_.sort(key=lambda x:(x[1],x[0]))
endtime = 0
count = 0
for i in range(len(class_)):
    if class_[i][0] >= endtime:
        endtime = class_[i][1]
        count += 1
print(count)