import math
T = int(input())
for t in range(T): 
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    if math.sqrt((x1-x2)**2+(y1-y2)**2)==0 and r1 == r2:
        print(-1)

    elif math.sqrt((x1-x2)**2+(y1-y2)**2)==r1+r2 or math.sqrt((x1-x2)**2+(y1-y2)**2)==abs(r1-r2):
        print(1)
    
    elif math.sqrt((x1-x2)**2+(y1-y2)**2)>r1+r2 or math.sqrt((x1-x2)**2+(y1-y2)**2)<abs(r1-r2):
        print(0)

    else: print(2)

        