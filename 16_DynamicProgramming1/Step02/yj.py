import sys
T=int(sys.stdin.readline())

def fibo(x):
    zero=[1,0]
    one = [0,1]

    if x==0:
        return [1,0], [0,0]
    if x==1:
        return [0,0], [0, 1]

    for i in range(2,x+1):
        zero_num=zero[i-1]+zero[i-2]
        one_num =one[i-1]+one[i-2]
        zero.append(zero_num)
        one.append(one_num)
    #print(zero[x],one[x])
    return zero,one

for j in range(T):
    num = int(sys.stdin.readline())
    zero,one = fibo(num)
    print(zero[num],one[num])