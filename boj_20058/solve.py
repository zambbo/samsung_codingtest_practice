from collections import deque

N, Q = map(int, input().split())

two_pow = 2**N

board = [list(map(int, input().split())) for _ in range(two_pow)]

L_list = list(map(int, input().split()))

dy = [0, 1, 0, -1]
dx = [1, 0, -1 ,0]

def rotate(l: int):
    global N

    if l == 0: return

    sub_box_len = 2 ** l

    for i in range(0, two_pow, sub_box_len):
        for j in range(0, two_pow, sub_box_len):
            new_sub_board = [[0]*sub_box_len for _ in range(sub_box_len)]
            for k in range(sub_box_len):
                for m in range(sub_box_len):
                    new_sub_board[k][m] = board[i+k][j+m]
            new_sub_board = [list(ll) for ll in zip(*new_sub_board[::-1])]

            for k in range(sub_box_len):
                for m in range(sub_box_len):
                    board[i + k][j + m] = new_sub_board[k][m]

def melting():
    global melt_num, board
    new_board = [line[:] for line in board]
    for i in range(two_pow):
        for j in range(two_pow):
            ice_neighbor_count = 0

            if board[i][j] == 0: continue
            for ddy, ddx in zip(dy, dx):
                next_y = i + ddy
                next_x = j + ddx
                if ice_neighbor_count >=3: break
                if next_y < 0 or next_x < 0 or next_y >= two_pow or next_x >= two_pow:
                    pass
                elif board[next_y][next_x] > 0:
                    ice_neighbor_count += 1

            if ice_neighbor_count < 3:
                new_board[i][j] = max(0, board[i][j] - 1)

    board = [line[:] for line in new_board]

def print_board():
    for line in board:
        print(line)

def bfs():

    visited = [[False]*two_pow for _ in range(two_pow)]
    max_cnt = 0

    for i in range(two_pow):
        for j in range(two_pow):
            if visited[i][j]: continue
            if board[i][j] == 0: continue

            queue = deque()

            queue.append((i, j))
            visited[i][j] = True

            cnt = 1
            while queue:
                y, x = queue.pop()

                for ddy, ddx in zip(dy, dx):
                    next_y = y + ddy
                    next_x = x + ddx

                    if next_y < 0 or next_x < 0 or next_y >= two_pow or next_x >= two_pow: continue
                    elif board[next_y][next_x] == 0: continue
                    if visited[next_y][next_x]:
                        continue

                    visited[next_y][next_x] = True
                    cnt += 1
                    queue.append((next_y, next_x))
            max_cnt = max(cnt, max_cnt)
    return max_cnt






for L in L_list:
    rotate(L)
    melting()


ice_sum = sum(map(sum, board))
if ice_sum == 0:
    print(0)
    print(0)
else:
    print(ice_sum)
    print(bfs())
