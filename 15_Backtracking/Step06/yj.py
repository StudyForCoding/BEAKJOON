import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def possible(i, j):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if sudoku[i][k] in nums:
            nums.remove(sudoku[i][k])
        if sudoku[k][j] in nums:
            nums.remove(sudoku[k][j])

    a = (i//3)*3
    b = (j//3)*3
    for p in range(a, a+3):
        for q in range(b, b+3):
            if sudoku[p][q] in nums:
                nums.remove(sudoku[p][q])

    return nums



def dfs(x):
    if x == len(zeros): 
        for s in sudoku:
            print(' '.join(map(str, s)))

        sys.exit(0)

    else:
        (i, j) = zeros[x]
        possible_nums = possible(i, j)

        for num in possible_nums:
            sudoku[i][j] = num
            dfs(x + 1)
            sudoku[i][j] = 0

dfs(0)

