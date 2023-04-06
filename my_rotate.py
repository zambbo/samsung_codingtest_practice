
def rotate_right_90(board: list[list[int]]) -> list[list[int]]:
    new_board = [[0]*len(board) for _ in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[j][len(board)-1-i] = board[i][j]

    return new_board

def rotate_right_180(board: list[list[int]]) -> list[list[int]]:
    new_board = [[0]*len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[len(board)-1-i][len(board[0]) -1 -j] = board[i][j]

    return new_board

def rotate_right_270(board: list[list[int]]) -> list[list[int]]:
    new_board = [[0]*len(board) for _ in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[len(board[0])-1-j][i] = board[i][j]

    return new_board
'''
1 2
3 4
5 6

2 4 6 #270
1 3 5

6 5 #180
4 3
2 1

5 3 1 # 90
6 4 2
'''

a = [[1,2],[3,4],[5,6]]
print(a)

b = rotate_right_90(a)
print(b)

c = rotate_right_180(a)
print(c)

d = rotate_right_270(a)
print(d)
