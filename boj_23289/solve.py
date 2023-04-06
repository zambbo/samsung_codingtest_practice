from collections import deque

UP_WALL = 0
RIGHT_WALL = 1

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

R, C, K = map(int, input().split())


board = [[[0, [False]*2] for _ in range(C)] for _ in range(R)]  # (온도, [벽])
# 벽 [위, 오른쪽]

mask_board = [[0]*C for _ in range(R)]  # 가장자리 온도 줄이기 용
for i in range(R):
    for j in range(C):
        if i==0 or i==R-1: mask_board[i][j] = -1
        elif j==0 or j==C-1: mask_board[i][j] = -1
        else: mask_board[i][j] = 0

watch_cells = []

heater_ds = [ # 각 방향 별로 바람 이동
    [(0, 1), (-1, 1), (1, 1)],  # right
    [(0, -1), (1, -1), (-1, -1)],   # left
    [(-1, 0), (-1, -1), (-1, 1)],   # up
    [(1, 0), (1, -1), (1, 1)],  # down
]

check_wall = [  # 각 방향 마다 조사 해야 될 벽
    [
        [((0, 0), RIGHT_WALL)],
        [((0, 0), UP_WALL), ((-1, 0), RIGHT_WALL)],
        [((1, 0), UP_WALL), ((1, 0), RIGHT_WALL)]
    ],   # right
    [
        [((0, -1), RIGHT_WALL)],
        [((1, 0), UP_WALL), ((1, -1), RIGHT_WALL)],
        [((0, 0), UP_WALL), ((-1, -1), RIGHT_WALL)]
    ],    # left
    [
        [((0, 0), UP_WALL)],
        [((0, -1), RIGHT_WALL), ((0, -1), UP_WALL)],
        [((0, 0), RIGHT_WALL), ((0, 1), UP_WALL)]
    ], # up
    [
        [((1, 0), UP_WALL)],
        [((0, -1), RIGHT_WALL), ((1, -1), UP_WALL)],
        [((0, 0), RIGHT_WALL), ((1, 1), UP_WALL)]
    ]   # down
]

check_wall_diffusion = [    # 디퓨전에서 각 방향마다 조사해야 될 벽
    ((0, 0), RIGHT_WALL),   #   right
    ((0, -1), RIGHT_WALL),  #   left
    ((0, 0), UP_WALL),  #   up
    ((1, 0), UP_WALL)   #   down
]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

heaters = []    # ((i, j), d)

for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if line[j] == 5:
            watch_cells.append((i, j))
        elif line[j] != 0:
            heaters.append(((i, j), line[j] - 1))


W = int(input())

for _ in range(W):
    r, c, d = map(int, input().split())
    board[r-1][c-1][1][d] = True


def bfs(pos:tuple[int, int], d:int) -> None:
    y, x = pos
    first_heat = (y+dy[d], x+dx[d])
    queue = deque()

    visited = [[False]*C for _ in range(R)]

    queue.append((first_heat, 5))

    while queue:
        (y, x), temperature = queue.popleft()

        board[y][x][0] += temperature

        temperature -= 1

        if temperature == 0: continue

        for idx, (ddy, ddx) in enumerate(heater_ds[d]):
            next_y = y + ddy
            next_x = x + ddx

            if next_y >= R or next_y < 0 or next_x >= C or next_x < 0: continue
            if visited[next_y][next_x] == True: continue

            wall_flag = False

            for (check_dy, check_dx), wall in check_wall[d][idx]:
                next_check_y = y + check_dy
                next_check_x = x + check_dx

                if next_check_y >= R or next_check_x >= C or next_check_y < 0 or next_check_x <0: continue
                if board[next_check_y][next_check_x][1][wall]:
                    wall_flag = True
                    break
            if wall_flag: continue



            visited[next_y][next_x] = True
            queue.append(((next_y, next_x), temperature))


def diffusion():
    new_board = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            total_diff = 0
            for d in range(4):
                next_y = i + dy[d]
                next_x = j + dx[d]

                if next_y < 0 or next_x < 0 or next_y >= R or next_x >= C: continue

                next_check_y = i + check_wall_diffusion[d][0][0]
                next_check_x = j + check_wall_diffusion[d][0][1]
                next_check_wall = check_wall_diffusion[d][1]

                if board[next_check_y][next_check_x][1][next_check_wall]: continue

                if board[i][j][0] <= board[next_y][next_x][0]: continue

                diff = board[i][j][0] - board[next_y][next_x][0]

                new_board[next_y][next_x] += diff // 4

                total_diff += diff // 4

            new_board[i][j] += board[i][j][0] - total_diff

    for i in range(R):
        for j in range(C):
            board[i][j][0] = new_board[i][j]

def decrease_border():
    for i in range(R):
        for j in range(C):
            board[i][j][0] += mask_board[i][j]
            board[i][j][0] = 0 if board[i][j][0] < 0 else board[i][j][0]

def finish() -> bool:
    return all(board[i][j][0] >= K for i, j in watch_cells)

def print_board(board):
    for i in range(R):
        for j in range(C):
            print(board[i][j][0], end=" ")
        print()

cookie = 0
while True:
    for heater in heaters:
        bfs(*heater)


    diffusion()

    decrease_border()

    cookie += 1

    if cookie > 100:
        print(101)
        break
    if finish():
        print(cookie)
        break

