from collections import deque

M, S = map(int, input().split())

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dy = [-1, 0, 1, 0]
shark_dx = [0, -1, 0, 1]

debug_shark_d = {
    0: "UP",
    1: "LEFT",
    2: "DOWN",
    3: "RIGHT"
}

debug_fish_d = {
    0: "LEFT",
    1: "LEFTUP",
    2: "UP",
    3: "RIGHTUP",
    4: "RIGHT",
    5: "RIGHTDOWN",
    6: "DOWN",
    7: "LEFTDOWN"
}


board = [[[0]*8 for _ in range(4)] for _ in range(4)]

fish_smell = [[0]*4 for _ in range(4)]

duplicate_fish = []

for _ in range(M):
    y, x, d = map(int,input().split())

    board[y-1][x-1][d-1] += 1

shark_y, shark_x = map(int, input().split())
shark_y -= 1
shark_x -= 1

def duplicate_save():
    global duplicate_fish
    for i in range(4):
        for j in range(4):
            for k in range(8):
                if board[i][j][k] != 0:
                    duplicate_fish.append(((i, j, k), board[i][j][k]))

def duplicate_spell():
    global duplicate_fish
    for (i, j, k), value in duplicate_fish:
        board[i][j][k] += value
    duplicate_fish = []

def fish_move():
    global board, fish_smell
    new_board = [[[0]* 8 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(8):
                if board[i][j][k] == 0: continue

                for l in range(8):

                    cur_d = (k - l) % 8

                    next_y = i + dy[cur_d]
                    next_x = j + dx[cur_d]

                    if 0<= next_y < 4 and 0<= next_x < 4 and \
                            (next_y != shark_y or next_x != shark_x) \
                            and fish_smell[next_y][next_x] == 0:
                        new_board[next_y][next_x][cur_d] += board[i][j][k]
                        new_board[i][j][k] -= board[i][j][k]
                        break

    for i in range(4):
        for j in range(4):
            for k in range(8):
                board[i][j][k] += new_board[i][j][k]

def get_dict(d_list: list) -> int:
    return (d_list[0]+1)*100 + (d_list[1]+1)* 10 + d_list[2]
def get_shark_move():
    d_list = backtracking(shark_y, shark_x, [], 0, 0)
    d_list.sort(key = lambda x: (-x[1], get_dict(x[0])))
    return d_list[0][0]


def backtracking(y:int, x:int, prev_d_list: list, depth:int, prev_catched_fishes:int ):
    global board
    if depth==3:
        return [(prev_d_list, prev_catched_fishes)]

    possible_d_list = []

    for d in range(4):
        next_y = y + shark_dy[d]
        next_x = x + shark_dx[d]

        if next_y < 0 or next_x < 0 or next_y >= 4 or next_x >=4:
            continue

        fishes = []

        catched_fishes = 0
        for i in range(8):
            catched_fishes += board[next_y][next_x][i]
            fishes.append(board[next_y][next_x][i])
            board[next_y][next_x][i] = 0

        next_d_list = prev_d_list[:]
        next_d_list.append(d)

        possible_d_list += backtracking(next_y, next_x, next_d_list, depth+1, prev_catched_fishes + catched_fishes)

        for i in range(8):
            board[next_y][next_x][i] = fishes[i]

    return possible_d_list

def kill_fish():
    global shark_y, shark_x, board, fish_smell
    d_list = get_shark_move()
    for d in d_list:
        shark_y += shark_dy[d]
        shark_x += shark_dx[d]

        killed_fish = 0
        for i in range(8):
            if board[shark_y][shark_x][i]: killed_fish += board[shark_y][shark_x][i]
            board[shark_y][shark_x][i] = 0

        if killed_fish:
            fish_smell[shark_y][shark_x] = 3
def decrease_fish_smell():
    for i in range(4):
        for j in range(4):
            fish_smell[i][j] = max(fish_smell[i][j]-1, 0)

for _ in range(S):
    duplicate_save()
    fish_move()
    kill_fish()
    decrease_fish_smell()
    duplicate_spell()

fish_sum = 0

for i in range(4):
    for j in range(4):
        for k in range(8):
            fish_sum += board[i][j][k]
print(fish_sum)

