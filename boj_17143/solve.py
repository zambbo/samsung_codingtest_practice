
R = 0
C = 0

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4


SHARKS = set()

class Shark:
    def __init__(self, velocity, direct, size):
        self.velocity = velocity
        self.direct = direct
        self.size = size

    def __str__(self):
        return f"velocity: {self.velocity}\ndirect: {self.direct}\nsize: {self.size}"

def fishing(board: list[list]) -> int:
    global R, C, SHARKS

    shark_sum = 0
    for j in range(C):
        # fishing
        for i in range(R):
            if board[i][j]:
                shark_sum += board[i][j].size
                board[i][j] = 0
                SHARKS.remove((i, j))
                break
        # moving
        moving(board)
    return shark_sum

def moving(board: list[list]) -> None:
    global R, C, SHARKS
    temp_sharks = dict()
    for y, x in SHARKS:
        shark = board[y][x]
        board[y][x] = 0
        
        cur_y = y
        cur_x = x

        cur_v = shark.velocity
        if shark.direct == UP:
            while cur_v:
                
                if shark.direct == DOWN:
                    move_available = R - 1 - cur_y
                    move_y = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_y += move_y
                    if cur_y == R - 1: shark.direct = UP
                elif shark.direct == UP:
                    move_available = cur_y
                    move_y = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_y -= move_y
                    if cur_y == 0: shark.direct = DOWN            
        elif shark.direct == DOWN:
            while cur_v:

                if shark.direct == DOWN:
                    move_available = R - 1 - cur_y
                    move_y = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_y += move_y
                    if cur_y == R - 1: shark.direct = UP
                elif shark.direct == UP:
                    move_available = cur_y
                    move_y = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_y -= move_y
                    if cur_y == 0: shark.direct = DOWN      

        elif shark.direct == LEFT:
            while cur_v:
            
                if shark.direct == RIGHT:
                    move_available = C - 1 - cur_x
                    move_x = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_x += move_x
                    if cur_x == C - 1: shark.direct = LEFT
                elif shark.direct == LEFT:
                    move_available = cur_x
                    move_x = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_x -= move_x
                    if cur_x == 0: shark.direct = RIGHT
        elif shark.direct == RIGHT:
            while cur_v:

                if shark.direct == RIGHT:
                    move_available = C - 1 - cur_x
                    move_x = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_x += move_x
                    if cur_x == C - 1: shark.direct = LEFT
                elif shark.direct == LEFT:
                    move_available = cur_x
                    move_x = cur_v if cur_v < move_available else move_available
                    cur_v = cur_v - move_available if cur_v >= move_available else 0
                    cur_x -= move_x
                    if cur_x == 0: shark.direct = RIGHT
        
        if (cur_y, cur_x) not in temp_sharks:
            temp_sharks[(cur_y, cur_x)] = []
            temp_sharks[(cur_y, cur_x)].append(shark)
        else:
            temp_sharks[(cur_y, cur_x)].append(shark)

    temp_sharks = {k:max(v, key=lambda shark: shark.size) for k, v in temp_sharks.items()}
    for (y, x), shark in temp_sharks.items():
        board[y][x] = shark
    
    SHARKS = set(temp_sharks.keys()) 
    
        


def main():
    global R, C
    R, C, M = map(int, input().strip().split())

    board = [[0]*C for _ in range(R)]
    
    for _ in range(M):
        y, x, v, d, s = map(int, input().strip().split())
        if d == 1 or d == 2:
            v %= (R-1)*2
        elif d == 3 or d == 4:
            v %= (C-1)*2
        shark = Shark(v, d, s)
        SHARKS.add((y-1, x-1))
         
        board[y-1][x-1] = shark

    shark_sum = fishing(board)
    print(shark_sum)
if __name__ == "__main__":
    main()
