import sys
from collections import deque
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    doc_size,my_doc = map(int,input().split())
    importance = list(map(int,input().split()))
    count = 0
    doc = deque()

    for imp in importance:
        doc.append(imp)

    while True:
        count += 1
        most_important_doc = doc.index(max(doc))
        doc.rotate(-most_important_doc)
        if my_doc < most_important_doc:
            # 내 문서가 가장 중요한 문서보다 앞 순서일 때 초기화되는 순서
            my_doc -= (most_important_doc + 1)
            my_doc += len(doc)
        elif my_doc > most_important_doc:
            # 내 문서가 가장 중요한 문서보다 뒷 순서일 때 초기화되는 순서
            my_doc -= (most_important_doc + 1)
        else:
            # 내 문서가 가장 중요한 문서이거나 가장 앞 순서일 때
            print(count)
            break
        doc.popleft()