t = int(input())
called = [[1,0],[0,1]]
for test in range(t):
    n = int(input())
    for i in range(2,n+1):
        if i < len(called):
            continue
        called.append([called[i-1][0]+called[i-2][0],called[i-1][1]+called[i-2][1]])
    print(" ".join(map(str,called[n])))