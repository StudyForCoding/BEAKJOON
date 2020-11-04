while(1):
    a,b = map(int,input().split())
    if a==0 and b==0:
        exit(0)
    elif (a!=0 and b==0) or (a==0 and b!=0):
        print('neither')
    elif a%b==0:
        print('multiple')
    elif b%a==0:
        print('factor')
    else:
        print('neither')