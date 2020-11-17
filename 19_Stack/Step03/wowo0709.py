import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    ps = list(input()) # 일부러 개행문자 '\n'을 포함
    count = 0
    for p in ps:
        if p == '(':
            count += 1
        elif p == ')':
            if count != 0:
                count -= 1
            else: # ')'가 많은 경우
                print('NO')
                break
        else: # 개행문자 '\n'을 이용해 끝임을 판단
            if count != 0: # '('가 많은 경우
                print('NO')
            else:
                print('YES')