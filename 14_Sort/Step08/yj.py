import sys
input = sys.stdin.readline

N = int(input())
words=set()
for i in range(N):
    word = input().rstrip()
    words.add((word,len(word)))
words = sorted(words, key= lambda x:(x[1],x[0]))

for i in words:
    print(i[0])