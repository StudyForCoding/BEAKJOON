import sys
square_list = [[False for i in range(9)] for j in range(9)]
line_list = [[False for i in range(9)] for j in range(9)]
column_list = [[False for i in range(9)] for j in range(9)]
board = [[int(x) for x in sys.stdin.readline().split()] for y in range(9)]
blank_list = []
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blank_list.append([i,j])
      continue
    square_list[(i//3)*3 + (j//3)][board[i][j]-1] = True
    line_list[i][board[i][j]-1] = True
    column_list[j][board[i][j]-1] = True

def sudoku(i,j):
  if i == 9:
    for line in range(9):
      sys.stdout.write(" ".join(map(str,board[line]))+"\n")
    sys.exit()

  for num in range(9):
    if square_list[(i//3)*3 + (j//3)][num] or line_list[i][num] or column_list[j][num]:
      continue
    board[i][j] = num+1
    blank_list.remove([i,j])
    square_list[(i//3)*3 + (j//3)][board[i][j]-1] = True
    line_list[i][board[i][j]-1] = True
    column_list[j][board[i][j]-1] = True
    if not blank_list:
      sudoku(9,9)
    sudoku(blank_list[0][0],blank_list[0][1])
    blank_list.insert(0,[i,j])
    square_list[(i//3)*3 + (j//3)][board[i][j]-1] = False
    line_list[i][board[i][j]-1] = False
    column_list[j][board[i][j]-1] = False
  return

sudoku(blank_list[0][0],blank_list[0][1])