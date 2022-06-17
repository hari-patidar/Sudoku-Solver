
def solve(bo):

    position = find_empty(bo)
    if not position:
        return True
    else:
        row, col = position
        
    for i in range(1, 10):
        if isValid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

def isValid(board, num, pos):
    
    row = pos[0]
    col = pos[1]

    #check row
    for i in range(len(board[0])):
        if i != row and board[row][i] == num:
            return False
    
    #check column
    for i in range(len(board)):
        if i != col and board[i][col] == num:
            return False

    #check square
    row_no = row // 3
    col_no = col // 3
    for i in range(row_no * 3, (row_no * 3) + 3):
        for j in range(col_no * 3, (col_no * 3) + 3):
            if board[i][j] == num and  (i, j) != (row, col):
                return False

    return True

def print_board(board):
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])
        
            else:
                print(str(board[i][j]) + " ", end = "")

def find_empty(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None

board = [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7]
]

print_board(board)
solve(board)
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
print_board(board)
