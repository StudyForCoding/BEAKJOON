C = int(input())
for i in range(C):
    num=0
    student,*score = map(int,input().split())
    for s in score:
        if s>sum(score)/student:
            num+=1
    print('%.3f'%round((num/student)*100,3)+'%')