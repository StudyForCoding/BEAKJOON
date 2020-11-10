N, M = map(int, input().split())

def cnt2(N): #2의 개수
    N_2 = 0
    while(N != 0): #N을 2로 나눴을 때 2의 배수가 N안에 몇개 있는지 체크
        N //= 2
        N_2 += N
    print(N_2)
    return N_2

def cnt5(N): #N을 5로 나눴을 때 5의 배수가 N안에 몇개 있는지 체크
    N_5 = 0
    while(N != 0):
        N //= 5
        N_5 += N
    print(N_5)
    return N_5

print(min(cnt2(N)-cnt2(M)-cnt2(N-M), cnt5(N)-cnt5(M)-cnt5(N-M)))
#N에서 2의개수-M에서 2의개수-(N-M에서 2의개수)
