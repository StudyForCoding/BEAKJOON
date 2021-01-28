import sys
input = sys.stdin.readline

minus_one, zero, plus_one = 0,0,0

def number_of_paper(n,matrix):
    global minus_one,zero,plus_one
    if n == 1:
        if matrix[0][0] == -1:  minus_one += 1
        elif matrix[0][0] == 0:  zero += 1
        else:  plus_one += 1
        return

    cnt_minus_one, cnt_zero, cnt_plus_one = 0,0,0

    for row in matrix:
        cnt_minus_one += row.count(-1)
        cnt_zero += row.count(0)
        cnt_plus_one += (n - cnt_minus_one - cnt_zero)

    if cnt_minus_one == n**2:  minus_one += 1
    elif cnt_zero == n**2:  zero += 1
    elif cnt_plus_one == n**2:  plus_one += 1
    else:  
        number_of_paper(n//3,[row[:n//3] for row in matrix[:n//3]])
        number_of_paper(n//3,[row[n//3:2*n//3] for row in matrix[:n//3]])
        number_of_paper(n//3,[row[2*n//3:] for row in matrix[:n//3]])
        number_of_paper(n//3,[row[:n//3] for row in matrix[n//3:2*n//3]])
        number_of_paper(n//3,[row[n//3:2*n//3] for row in matrix[n//3:2*n//3]])
        number_of_paper(n//3,[row[2*n//3:] for row in matrix[n//3:2*n//3]])
        number_of_paper(n//3,[row[:n//3] for row in matrix[2*n//3:]])
        number_of_paper(n//3,[row[n//3:2*n//3] for row in matrix[2*n//3:]])
        number_of_paper(n//3,[row[2*n//3:] for row in matrix[2*n//3:]])
        


n = int(input())
matrix = [[int(x) for x in input().rstrip().split()] for _ in range(n)]
number_of_paper(n,matrix)
print(minus_one,zero,plus_one,sep = '\n')