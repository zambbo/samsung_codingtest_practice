#   기본적으로 어항은 위에서 아래로 자란다.
#   위에서 아래로 자란다는 것은 바닥이 0행이라는 것이다.
#   열은 그대로이다.
# 5 3 3 14 9 3 11 8

N, K = map(int, input().split())

board = [[0]*N for _ in range(N)]

board[0] = list(map(int, input().split()))

# 3 3 14 9 3 11 8
# 5

# 3 14 9 3 11 8
# 3 5

# 1 만큼 row를 띄워야한다. (첫번째 쌓는 거 제외)
# col_len 만큼 옆으로 이동한다.
# 현재 row_len이 다음의 col_len이 된다.
# 현재 row_len과 col_len 값이 같으면 다음 회전뒤에 row_len값이 1늘어난다.

# 9 4 11 8
# 14 5
# 3 3

# 좌 우 하 상
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

def add_fish_to_board():
    min_fish = min(board[0])

    for i in range(N):
        if board[0][i] == min_fish: board[0][i] += 1

def levitation():
    fishbowl_row_len = 2
    fishbowl_col_len = 1
    start_index = 1

    board[1][1] = board[0][0] # 처음에 쌓기
    board[0][0] = 0

    while True:
        #한번 돌려보면 알 수 있는 탈출 조건
        #
        if start_index + fishbowl_col_len + fishbowl_row_len>= N+1: break

        for i in range(fishbowl_row_len):
            for j in range(fishbowl_col_len):
                # 문제와 달리 아래로 자라기 때문에 오른쪽으로 90도 회전하는 것이 아니라 왼쪽으로 90도 회전해준다.
                # 그리고 현재 index (가장 왼쪽 바닥의 인덱스) 와 현재 덩어리의 행, 열 길이를 고려하여 적절히 넣어준다.
                board[fishbowl_col_len -1 - j + 1][i +start_index + fishbowl_col_len] = board[i][j + start_index]
                board[i][j + start_index] = 0

        start_index += fishbowl_col_len
        if fishbowl_col_len == fishbowl_row_len:
            fishbowl_row_len += 1
        else:
            fishbowl_col_len = fishbowl_row_len

    return start_index, fishbowl_row_len, fishbowl_col_len


def adjust_fishes(start_index: int, fishbowl_row_len: int, fishbowl_col_len: int):
    global board

    new_board = [[0]*N for _ in range(N)]

    remain_start_index = start_index + fishbowl_col_len

    for i in range(fishbowl_row_len):
        for j in range(fishbowl_col_len):
            escape_fish = 0
            for d in range(4):
                next_y = i + dy[d]
                next_x = start_index + j + dx[d]

                # 만약 꼬리부분과 붙어 있는 인덱스라면 우측도 확인
                if i==0 and j == fishbowl_col_len -1 and d==1:
                    if next_x >= N: continue # 꼬리부분이 없을때
                    if board[i][start_index+j] > board[next_y][next_x]:
                        cur_escape_fish = (board[i][start_index+j] - board[next_y][next_x]) // 5
                        escape_fish += cur_escape_fish
                        new_board[next_y][next_x] += cur_escape_fish

                if next_y < 0 or next_x < start_index or next_y >= fishbowl_row_len or next_x >= remain_start_index:
                    continue

                if board[i][start_index+j] > board[next_y][next_x]:
                    cur_escape_fish = (board[i][start_index + j] - board[next_y][next_x]) // 5
                    escape_fish += cur_escape_fish
                    new_board[next_y][next_x] += cur_escape_fish

            new_board[i][start_index + j] += board[i][start_index + j] - escape_fish

    # 만약 꼬리부분이 있으면 좌우만 본다
    for i in range(remain_start_index, N):
        escape_fish = 0
        for d in range(2):
            next_x = i + dx[d]

            if next_x >= N: continue #보드를 넘어갔으면

            if board[0][i] > board[0][next_x]:
                cur_escape_fish = (board[0][i] - board[0][next_x]) // 5
                escape_fish += cur_escape_fish
                new_board[0][next_x] += cur_escape_fish

        new_board[0][i] += board[0][i] - escape_fish

    board = [line[:] for line in new_board]

def print_board():
    for line in board:
        print(line)
    print("-"*100)

def serialize(start_index: int, fishbowl_row_len:int, fishbowl_col_len:int) -> None:
    global board
    idx = 0

    for j in range(fishbowl_col_len):
        for i in range(fishbowl_row_len):
            board[0][idx] = board[i][start_index + j]
            board[i][start_index + j] = 0
            idx += 1

def flip() -> tuple[int, int, int]:
    global board

    first_step_row_len = N // 2
    for i in range(first_step_row_len):
        board[1][N-1-i] = board[0][i]
        board[0][i] = 0

    start_index = N//2
    second_step_row_len = 2
    second_step_col_len = N // 4

    for i in range(second_step_row_len):
        for j in range(second_step_col_len):
            board[4 - 1 - i][N-1-j]  = board[i][start_index + j]
            board[i][start_index+j] = 0

    start_index = N // 2 + N // 4
    fishbowl_col_len = N // 4
    fishbowl_row_len =  4

    return start_index, fishbowl_row_len, fishbowl_col_len

cnt = 0
while True:
    add_fish_to_board()
    start_index, fishbowl_row_len, fishbowl_col_len = levitation()
    adjust_fishes(start_index, fishbowl_row_len, fishbowl_col_len)
    serialize(start_index, fishbowl_row_len, fishbowl_col_len)
    start_index, fishbowl_row_len, fishbowl_col_len = flip()
    adjust_fishes(start_index, fishbowl_row_len, fishbowl_col_len)
    serialize(start_index, fishbowl_row_len, fishbowl_col_len)
    cnt += 1
    diff = max(board[0]) - min(board[0])
    if diff <= K:
        print(cnt)
        break
