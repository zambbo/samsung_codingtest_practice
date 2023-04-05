N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
magic = []
waters = []

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    magic.append(tuple(map(int,input().split())))

def move(d: int, s:int):
    global clouds, waters
    ddy = dy[d]
    ddx = dx[d]

    for y, x in clouds:
        next_y = (y + ddy*s) % N
        next_x = (x + ddx*s) % N

        board[next_y][next_x] += 1

        waters.append((next_y, next_x))
        visited[next_y][next_x]= True

    clouds = []

def add_water():
    global waters

    for y, x in waters:
        w = 0

        for d in [1, 3, 5, 7]:
            ddy = dy[d]
            ddx = dx[d]

            next_y = y + ddy
            next_x = x + ddx

            if 0<= next_x < N and 0<= next_y < N and board[next_y][next_x] != 0:
                w += 1

        board[y][x] += w

def make_cloud():
    global clouds, waters

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                visited[i][j] = False
                continue

            if board[i][j] >= 2:
                board[i][j] -= 2
                clouds.append((i, j))

    waters = []





for d, s in magic:
    move(d-1, s)
    add_water()
    make_cloud()

print(sum(map(sum, board)))

