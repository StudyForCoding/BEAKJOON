N = int(input())
num=1
a=1
room=6

if N==1: print(1)
else: 
    while (a<N):
        a+=room
        room+=6
        num+=1
    print(num)