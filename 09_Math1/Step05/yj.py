A,B,V = map(int,input().split())
num =0
if (V-B)%(A-B)==0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B) +1)