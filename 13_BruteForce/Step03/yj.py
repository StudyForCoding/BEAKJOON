N= int(input())
dungchi =[]
for n in range(N):
    dung=list(map(int,input().split()))
    dungchi.append(dung)
    
rank=[]
for dung in dungchi:
    n=1
    for i in range(len(dungchi)):
        if dung[0]<dungchi[i][0] and dung[1]<dungchi[i][1]:
            n+=1
    rank.append(n)

print(' '.join(map(str,rank)))