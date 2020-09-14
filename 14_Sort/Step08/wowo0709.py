import sys
N = int(input())
word_set = set()
for i in range(N):
  word_set.add(sys.stdin.readline())
word_list = sorted(list(word_set),key = lambda w: (len(w),w))
for word in word_list:
  sys.stdout.write(word)