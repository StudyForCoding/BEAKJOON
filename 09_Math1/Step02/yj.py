N = int(input())
box=0
while N>0:
    if N%5==0:
        N-=5
        box+=1
    elif N%3 ==0:
        N-=3
        box+=1
    elif N>5:
        N-=5
        box+=1
    else: 
        box=-1
        break
print(box)