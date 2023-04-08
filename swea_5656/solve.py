from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())

visited = []
exploited_poses = []

def print_board():
        global board

        for line in board:
                print(line)
        print("-" * 100)


def dropped():
        global board, W, H

        for j in range(W):
                pointer = H - 1
                for i in range(H - 1, -1, -1):
                        if board[i][j] == 0:
                                continue

                        elif board[i][j] != 0:
                                if board[pointer][j] == 0:
                                        board[pointer][j] = board[i][j]
                                        board[i][j] = 0
                                pointer -= 1


def backtracking(depth):
        global N, W, H, MAX_BLOCK_NUM, board, exploited_poses

        if depth == N:
                block_num = get_block_num()
                MAX_BLOCK_NUM = min(MAX_BLOCK_NUM, block_num)
                #print_board()
                return

        all_zero = 0
        for i in range(W):
                y, x = get_top_block(i)

                if y == -1:
                        all_zero += 1
                        continue

                bfs(y, x)
                capture_board = [line[:] for line in board]
                erase()
                dropped()

                backtracking(depth + 1)
                board = [line[:] for line in capture_board]

        if all_zero == W:
                MAX_BLOCK_NUM = 0
                return
def bfs(sy, sx):
        global W, H, board, q, visited, exploited_poses

        y, x = sy, sx

        exploited_poses = []

        visited = [[False]*W for _ in range(H)]

        q.append((sy, sx))

        while q:

                y, x = q.popleft()

                exploited_poses.append((y, x, board[y][x]))

                if board[y][x] == 1: continue

                for i in range(1, board[y][x]):
                        for d in range(4):
                                next_y, next_x = y + dy[d]*i, x + dx[d]*i
                                if next_y < 0 or next_x < 0 \
                                        or next_y >=H or next_x >= W: continue
                                if visited[next_y][next_x] or board[next_y][next_x] == 0:continue

                                visited[next_y][next_x] = True

                                q.append((next_y, next_x))


def erase():
        global board, exploited_poses

        for y, x, value in exploited_poses:
                board[y][x] = 0

def get_block_num():
        global board, W, H
        block_num = 0
        for i in range(H):
                for j in range(W):
                        if board[i][j] != 0:
                                block_num += 1

        return block_num

def get_top_block(line_idx):
        global H, board

        top_block_y = -1
        for j in range(H):
                if board[j][line_idx] != 0:
                        top_block_y = j
                        break

        return (top_block_y, line_idx)

for tc in range(1, T+1):

        N, W, H = map(int, input().split())

        board = [list(map(int, input().split())) for _ in range(H)]

        q = deque()
        # 좌표 값을 받아서 현재 좌표 에서 부터 터뜨릴 수 있는 애들 좌표 배열 반환


        MAX_BLOCK_NUM = float('inf')
        backtracking(0)

        print(f"#{tc} {MAX_BLOCK_NUM}")
