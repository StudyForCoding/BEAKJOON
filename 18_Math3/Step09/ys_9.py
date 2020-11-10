import sys
N = int(sys.stdin.readline()) #테스트케이스 수

for i in range(N):
    n = int(sys.stdin.readline()) #옷 종류
    
    wear = []
    for i in range(n):
        wear.append(sys.stdin.readline().split()[1])

    wearset = tuple(set(wear)) #옷 종류별로 나눔

    type = []
    for i in range(len(wearset)): #옷 종류 개수 
        type.append(wear.count(wearset[i]))

    result = 1
    for t in type:
        result *= (t + 1) #쓰지않는 경우까지 고려(+1)

    print(result - 1) #알몸인 경우 뺌
