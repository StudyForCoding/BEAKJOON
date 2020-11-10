test = int(input())
c_type = dict()
for t in range(test):
    n = int(input())
    # 딕셔너리로 의상의 종류별 개수 세기
    for i in range(n):
        type_ = list(input().split())[1]
        c_type[type_] = c_type.get(type_,0) + 1
    answer = 1
    # answer = (종류별 의상 개수+1)의 총 곱 - 1
    for v in c_type.values():
        answer *= (v+1)
    print(answer - 1)
    c_type.clear()