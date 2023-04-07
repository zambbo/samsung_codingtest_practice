LEFT_BLIZARD = []
DOWN_BLIZARD = []
RIGHT_BLIZARD = []
UP_BLIZARD = []

BLIZARDS = [LEFT_BLIZARD, DOWN_BLIZARD, RIGHT_BLIZARD, UP_BLIZARD]

'''
왼쪽: (0, 9, 26)
아래쪽: (2, 13, 32)
오른쪽: (4, 17, 38)
위쪽: (6, 21, 44)
'''

# 블리자드 인덱스 저장
offset = 0
increase_amount = 1

for i in range(49//2):
    for idx, blizard in enumerate(BLIZARDS):
        blizard.append(offset)
        if idx == 0 or idx == 3: increase_amount += 1
        offset += increase_amount

# 상 하 좌 우 로 변경 (d입력값이랑 맞추려고)
BLIZARDS = [[], BLIZARDS[3], BLIZARDS[1], BLIZARDS[0], BLIZARDS[2]]

ONE_BALL = 0
TWO_BALL = 0
THREE_BALL = 0


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

spells = [list(map(int, input().split())) for _ in range(M)]

IDX_LIMIT = N*N -1 -1 # 상어 위치를 제외한 최대 인덱스

turn_left = lambda x: (-x[1], x[0])

def flatten(board: list[list[int]]) -> list[int]:
    global MAX_LENGTH
    flattened_board = []
    shark_y = N // 2
    shark_x = N // 2

    # 기존에는 왼쪽으로 이동
    ddy = 0
    ddx = -1

    velocity = 1

    cur_y = shark_y
    cur_x = shark_x

    # N - 2 만큼 2번씩 움직이고
    # 마지막 한번은 3번 움직임
    for i in range(N-2):
        for j in range(2):
            for _ in range(velocity):
                cur_y = cur_y + ddy
                cur_x = cur_x + ddx

                if board[cur_y][cur_x] == 0: return flattened_board

                flattened_board.append(board[cur_y][cur_x])
            ddy, ddx = turn_left((ddy, ddx))

        velocity += 1

    for i in range(3):
        for _ in range(velocity):
            cur_y = cur_y + ddy
            cur_x = cur_x + ddx

            if board[cur_y][cur_x] == 0: return flattened_board

            flattened_board.append(board[cur_y][cur_x])
        ddy, ddx = turn_left((ddy, ddx))

    return flattened_board

flattened_board = flatten(board)

def explosion() -> None:
    global flattened_board, ONE_BALL, TWO_BALL, THREE_BALL

    MAX_LENGTH = len(flattened_board)
    cur_max_length = MAX_LENGTH

    while True:
        start_index = 0
        length = 0
        for idx, value in enumerate(flattened_board):
            if idx == 0 or flattened_board[idx] != flattened_board[idx-1]: #만약 연속성이 끊겼다면
                if length >= 4: #만약 폭발한다면
                    if flattened_board[idx - 1] == 1:
                        ONE_BALL += length
                    elif flattened_board[idx - 1] == 2:
                        TWO_BALL += length
                    elif flattened_board[idx - 1] == 3:
                        THREE_BALL += length
                    for i in range(idx-1, start_index-1, -1): #연속한 친구들 -1로 초기화
                        flattened_board[i] = -1
                    cur_max_length -= length

                start_index = idx #끊겼으니 현재 부터 시작
                length = 1 #length는 1로 초기화 (현재 아이만 있으니깐)
            else: #연속성이 유지되고 있으면
                length += 1
                if idx == MAX_LENGTH - 1: #만약 마지막 인덱스라면
                    if length >= 4: #만약 폭발하면
                        if flattened_board[idx - 1] == 1:
                            ONE_BALL += length
                        elif flattened_board[idx - 1] == 2:
                            TWO_BALL += length
                        elif flattened_board[idx - 1] == 3:
                            THREE_BALL += length
                        for i in range(idx, start_index - 1, -1):  # 연속한 친구들 -1로 초기화
                            flattened_board[i] = -1
                        cur_max_length -= length

        if cur_max_length == MAX_LENGTH: # 만약에 4개 이상 연속한 아이가 없었다면
            break


        flattened_board = [value for value in flattened_board if value != -1]  # -1인 연속한 아이들 싹다 제거

        MAX_LENGTH = cur_max_length

def modified():
    global flattened_board

    new_flattened_board = [-1] * (len(flattened_board) * 2)

    new_idx = 0
    length = 0

    # board의 구슬 개수가 1개일때 예외처리
    if len(flattened_board) == 1:
        new_flattened_board[0] = 1
        new_flattened_board[1] = flattened_board[0]
        flattened_board = new_flattened_board[:]
        return

    for idx, value in enumerate(flattened_board):
        if idx == 0: # index 0은 따로 처리 (oob error 방지용)
            length += 1
            continue

        if idx == len(flattened_board) - 1: #만약에 현재가 마지막 인덱스라면
            if flattened_board[idx] != flattened_board[idx-1]: #만약에 연속성이 끊겼다면
                new_flattened_board[new_idx] = length

                if new_idx+1 > IDX_LIMIT: break

                new_flattened_board[new_idx+1] = flattened_board[idx-1]

                length = 1
                new_idx += 2
            else: # 만약에 연속성이 안끊겼다면
                length += 1

            if new_idx > IDX_LIMIT: break
            new_flattened_board[new_idx] = length
            if new_idx+1 > IDX_LIMIT: break
            new_flattened_board[new_idx+1] = flattened_board[idx]

        else: #만약에 현재가 마지막 인덱스가 아니라면
            if flattened_board[idx] != flattened_board[idx-1]: #만약에 연속성이 끊겼다면
                new_flattened_board[new_idx] = length
                if new_idx +1 > IDX_LIMIT: break
                new_flattened_board[new_idx+1] = flattened_board[idx-1]
                length = 1
                new_idx += 2
            else: #만약에 연속성이 끊기지 않았다면
                length += 1

        if new_idx > IDX_LIMIT:
            break

    flattened_board = [value for value in new_flattened_board if value != -1]


for d, s in spells:
    blizard_indices = BLIZARDS[d][:s]

    # 블리자드 마법 구현
    flattened_board = [value for idx, value in enumerate(flattened_board) if idx not in blizard_indices]

    explosion()

    modified()



print(ONE_BALL + 2*TWO_BALL + 3*THREE_BALL)


