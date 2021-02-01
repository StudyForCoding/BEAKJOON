'''딕셔너리로 구현하기'''
import sys
input = sys.stdin.readline

N = int(input())
cards = dict()
for card in list(map(int,input().split())):
    cards[card] = cards.get(card,0) + 1
M = int(input())
targets = list(map(int,input().split()))

for target in targets:
    print(cards.get(target,0),end=' ')