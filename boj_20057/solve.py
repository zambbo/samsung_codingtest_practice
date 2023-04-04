

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

tornado_y = N // 2
tornado_x = tornado_y

out_sand = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

right_rotate = lambda d: (d[1], -d[0])

left_rotate = lambda d: (-d[1], d[0])

def blow_move(y, x, ddy, ddx) -> list[tuple[tuple[int,int], float]]:
    possible_move = []
    for rotate in [right_rotate, left_rotate]:
        rot_ddy, rot_ddx = rotate((ddy, ddx))
        possible_move.append(((y+rot_ddy, x + rot_ddx), 0.01))

        next_y , next_x = y + ddy, x + ddx

        possible_move.append(((next_y + rot_ddy, next_x + rot_ddx), 0.07))
        possible_move.append(((next_y + rot_ddy * 2, next_x + rot_ddx * 2), 0.02))

        next_y, next_x = y + ddy*2, x + ddx*2

        possible_move.append(((next_y + rot_ddy, next_x + rot_ddx), 0.1))

    possible_move.append(((y + ddy * 3, x + ddx*3), 0.05))

    return possible_move

def is_out(y:int, x:int):
    return y < 0 or x < 0 or y >= N or x >= N

def blow(y:int, x:int, ddy: int, ddx: int):
    global out_sand
    sand = board[y+ddy][x+ddx]
    remain_sand = sand

    alpha_y = y + ddy*2
    alpha_x = x + ddx*2

    for (blow_y, blow_x), portion in blow_move(y, x, ddy, ddx):
        if is_out(blow_y, blow_x):
            remain_sand -= int(sand * portion)
            out_sand += int(sand * portion)
        else:
            remain_sand -= int(sand * portion)
            board[blow_y][blow_x] += int(sand * portion)

    if is_out(alpha_y, alpha_x):
        out_sand += remain_sand
    else:
        board[alpha_y][alpha_x] += remain_sand

    board[y][x] = 0

move_amount = 1
cur_ddy = 0
cur_ddx = -1


for _ in range(N-2):
    for _ in range(2):
        for _ in range(move_amount):
            blow(tornado_y, tornado_x, cur_ddy, cur_ddx)
            tornado_y += cur_ddy
            tornado_x += cur_ddx

        cur_ddy, cur_ddx = left_rotate((cur_ddy, cur_ddx))

    move_amount += 1

for i in range(3):
    for _ in range(move_amount):
        blow(tornado_y, tornado_x, cur_ddy, cur_ddx)
        tornado_y += cur_ddy
        tornado_x += cur_ddx
    cur_ddy, cur_ddx = left_rotate((cur_ddy, cur_ddx))

print(out_sand)
