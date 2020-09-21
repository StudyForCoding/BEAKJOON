import sys
from itertools import combinations
n = int(input())
s = [[int(index) for index in sys.stdin.readline().split()] for line in range(n)]
scorediff = [0]*(len(list(combinations(list(range(n)),n//2)))//2)
player_selected = [False]*n
count = 0
score1 = score2 = 0
team1 = team2 = []

def maketeam(n,cursor):
  global s,count,score1,score2
  if len(team1) == n//2:
    team2 = list(range(0,n))
    for player in team1:
      team2.remove(player)
    for i in range(n//2 -1):
      for j in range(i+1,n//2 ):
        score1 += s[team1[i]][team1[j]] + s[team1[j]][team1[i]]
        score2 += s[team2[i]][team2[j]] + s[team2[j]][team2[i]]
    scorediff[count] = abs(score1-score2)
    if count == len(scorediff)-1:
      print(min(scorediff))
      sys.exit()
    count += 1
    score1 = score2 = 0
    return

  for player in range(cursor,n):
    if player_selected[player] == True:
      continue
    team1.append(player)
    player_selected[player] = True
    maketeam(n,player+1)
    team1.remove(player)
    player_selected[player] = False

maketeam(n,0)