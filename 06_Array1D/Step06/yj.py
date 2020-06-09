test = int(input())
for i in range(test):
    score =0
    case = list(input())
    o=0
    for a in case:
        if a =='O':
            o+=1
        else:
            o=0
        score +=o
    print(score)