while True:
    tri=[]
    a,b,c = map(int,input().split())
    tri.append(a)
    tri.append(b)
    tri.append(c)
    if tri ==[0,0,0]:
         break
    tri = sorted(tri)
    if tri[0]**2 + tri[1]**2 ==tri[2]**2:
        print('right')
    else : 
        print('wrong')