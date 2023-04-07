
T = int(input())
for test_case in range(1, T+1):
        N, K = map(int, input().split())


        board = [list(map(int, input().split())) for _ in range(N)]

        dy = [-1, 1, 0, 0]
        dx = [0, 0, 1, -1]

        max_length = 0

        def dfs(y, x, depth, dig_flag):
                global max_length, N, K
                can_not_move = True

                for d in range(4):
                        next_y = y + dy[d]
                        next_x = x + dx[d]

                        if next_y < 0 or next_y >= N or next_x < 0 or next_x >=N or visited[next_y][next_x]: continue


                        if board[y][x] > board[next_y][next_x]:
                                can_not_move = False
                                visited[next_y][next_x] = True
                                dfs(next_y, next_x, depth + 1, dig_flag)
                                visited[next_y][next_x] = False

                        else: #만약 옆의 봉우리가 같거나 클 경우
                                diff = board[next_y][next_x] - board[y][x]
                                if K > diff: #만약 충분히 깎을 수 있을 때
                                        if dig_flag: #만약 기회가 있다면
                                                can_not_move = False
                                                temp = board[next_y][next_x]
                                                visited[next_y][next_x] = True
                                                board[next_y][next_x] = board[y][x] - 1
                                                dfs(next_y, next_x, depth+1, False)
                                                board[next_y][next_x] = temp
                                                visited[next_y][next_x] = False

                                else: #깎을 수 없을 때
                                        pass
                if can_not_move:
                        max_length = max(depth, max_length)

        def get_maximum_mountains():
                global board, N

                maximum_value = max(map(max, board))

                max_mountains = []

                for i in range(N):
                        for j in range(N):
                                if board[i][j] == maximum_value:
                                        max_mountains.append((i, j))
                return max_mountains

        max_mountains = get_maximum_mountains()
        visited = [[False]* N for _ in range(N)]

        for y, x in max_mountains:
                visited[y][x] = True
                dfs(y, x, 1, True)
                visited[y][x] = False

        print(f"#{test_case} {max_length}")
