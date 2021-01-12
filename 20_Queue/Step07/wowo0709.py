import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    empty = False
    func = list(input().rstrip()) # 함수 리스트
    len_of_mylist = int(input()) # 리스트의 길이
    # 숫자 리스트 만들기
    if len_of_mylist == 0:  
        empty = True
        __ = input()
    else:  mylist = list(map(int,input()[1:-2].split(',')))
    # 에러인 경우 거르기
    if len_of_mylist < func.count('D'):
        print('error')
        continue
    # 머리와 꼬리 인덱스 초기화
    head = 0
    tail = len_of_mylist-1
    # 함수 연산
    for f in func:
        if f == 'R': # 뒤집기
            head,tail = tail,head
        else: # 앞에서 하나 빼기
            if head < tail:
                head += 1
            elif head > tail:
                head -= 1
            else: # head == tail이면 원소가 하나 남음, D 연산을 할 경우 빈 리스트
                empty = True
                break
    # 리스트가 빈 경우 빈 리스트를 출력하고 다음 테스트 케이스
    if empty:
        print('[]')
        continue
    # 최종 결과 리스트 가져오기
    if head < tail:
        mylist = mylist[head:tail+1]
    elif head > tail:
        mylist = list(reversed(mylist[tail:head+1]))
    else: # 원소가 하나 남은 경우
        mylist = [mylist[head]]
    # 출력 양식
    for i in range(len(mylist)):
        if i == 0:
            print('[',sep='',end='')
        if i != len(mylist) - 1:
            print(mylist[i],',',sep='',end='')
        else:
            print(mylist[i],']',sep='')