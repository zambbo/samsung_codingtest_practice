from collections import deque

get_op_cost = lambda k: k*k + (k-1)*(k-1)

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
        N, M = map(int, input().split())

        board = [list(map(int,input().split())) for _ in range(N)]

        MAX = 0

        def bfs(sy:int, sx:int, k:int):
                global N, M, MAX
                q =  deque()

                house_num = 0

                op_cost = get_op_cost(k)

                visited = [[False]*N for _ in range(N)]

                visited[sy][sx] = True

                q.append((sy, sx))

                for i in range(k):
                        q_len = len(q)
                        for _ in range(q_len):
                                y, x = q.popleft()

                                if board[y][x] == 1: house_num += 1

                                for d in range(4):
                                        next_y, next_x = y + dy[d], x + dx[d]

                                        if next_y < 0 or next_x < 0 or next_x >= N or next_y >= N or visited[next_y][next_x]: continue

                                        visited[next_y][next_x] = True

                                        q.append((next_y, next_x))


                profit = house_num * M - op_cost

                if profit >= 0:
                        MAX = max(MAX, house_num)

        for i in range(N):
                for j in range(N):
                        for k in range(1, N+2):
                                bfs(i, j, k)

        print(f"#{tc} {MAX}")



