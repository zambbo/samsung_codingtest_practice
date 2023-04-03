from collections import deque

N = int(input())

board = []

baby_shark_pos = (0, 0)
baby_shark_size = 2

for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

    for j in range(N):
        if board[i][j] == 9:
            baby_shark_pos = (i, j)

dy = [0, 0, -1 ,1]
dx = [1, -1, 0, 0]

def bfs(baby_shark_pos: tuple[int, int]) -> list[tuple[int,int]]:
    queue = deque()
    visited = [[False]*N for _ in range(N)]

    y, x = baby_shark_pos
    visited[y][x] = True

    queue.append((baby_shark_pos, 0))

    eatable_sharks = []
    ret_dist = 10_000_000_000

    while queue:
        (y, x), dist = queue.popleft()

        dist += 1
        for ddy, ddx in zip(dy, dx):
            next_y = y + ddy
            next_x = x + ddx

            if next_y < 0 or next_x < 0 or next_y >= N or next_x >= N:
                continue

            if visited[next_y][next_x]:
                continue

            if baby_shark_size < board[next_y][next_x]:
                pass
            elif board[next_y][next_x] == 0 or baby_shark_size == board[next_y][next_x]:
                visited[next_y][next_x] = True
                queue.append(((next_y, next_x), dist))
            elif baby_shark_size > board[next_y][next_x]:
                if dist > ret_dist: continue
                visited[next_y][next_x] = True
                eatable_sharks.append((next_y, next_x))
                ret_dist = dist
            else:
                pass

    eatable_sharks.sort(key=lambda x: (x[0], x[1]))
    return eatable_sharks, ret_dist

dist = 0
eat_num = 0
while True:
    eatable_sharks, cur_dist = bfs(baby_shark_pos)

    if len(eatable_sharks) == 0:
        print(dist)
        break

    dist += cur_dist

    victim_y, victim_x = eatable_sharks[0]
    cur_y, cur_x = baby_shark_pos



    board[victim_y][victim_x] = 0
    board[cur_y][cur_x] = 0

    eat_num += 1
    if eat_num == baby_shark_size:
        baby_shark_size += 1
        eat_num = 0

    baby_shark_pos = (victim_y, victim_x)











