import sys
input = sys.stdin.readline

seq1,seq2 = list(input().rstrip()),list(input().rstrip())
l1,l2 = len(seq1),len(seq2)
LCS = [[[0,[]] for _ in range(l2+1)] for _ in range(l1+1)] # 최대길이,수열
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if seq1[i-1] == seq2[j-1]:
            LCS[i][j][0] = LCS[i-1][j-1][0]+1
            LCS[i][j][1] = LCS[i-1][j-1][1]+[seq2[j-1]]
        elif LCS[i-1][j][0] > LCS[i][j-1][0]:
            LCS[i][j][0] = LCS[i-1][j][0]
            LCS[i][j][1] = LCS[i-1][j][1]
        else:
            LCS[i][j][0] = LCS[i][j-1][0]
            LCS[i][j][1] = LCS[i][j-1][1]
LCS[l1].sort(key=lambda x:x[0])
ans1,ans2 = LCS[l1][l2][0],LCS[l1][l2][1]
print(ans1)
if ans1 != 0: print(''.join(ans2))