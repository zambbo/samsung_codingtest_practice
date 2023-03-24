from collections import deque


EMPTY=0
APPLE=1
SNAKE=2

N = 0

def turn_right(cur_direct: tuple[int, int]) -> tuple[int, int]:
	direct = (0, 0)
	if cur_direct == (0, 1): #right
		direct = (1, 0)
	elif cur_direct == (1, 0): #down
		direct = (0, -1)
	elif cur_direct == (0, -1): #left
		direct = (-1, 0)
	elif cur_direct == (-1, 0): #up
		direct = (0, 1)

	return direct

def turn_left(cur_direct: tuple[int, int]) -> tuple[int, int]:
	direct = (0, 0)
	if cur_direct == (0, 1): #right
		direct = (-1, 0)
	elif cur_direct == (1, 0): #down
		direct = (0, 1)
	elif cur_direct == (0, -1): #left
		direct = (1, 0)
	elif cur_direct == (-1, 0): #up
		direct = (0, -1)

	return direct	

def dummy(board: list[list[int]], handling: dict) -> int:
	global N

	direct = (0, 1)

	snake = deque()
	
	snake.append((0, 0))

	cur_time = 0
	while True:
		if cur_time in handling.keys():
			handle = handling[cur_time]
			direct = turn_right(direct) if handle == "D" else turn_left(direct)

		cur_time += 1
	
		cur_state = snake[-1]	
		next_y = cur_state[0] + direct[0]
		next_x = cur_state[1] + direct[1]
		
		if next_y >= N or next_x >= N or next_y < 0 or next_x < 0 or board[next_y][next_x] == SNAKE:
			return cur_time

		if board[next_y][next_x] == APPLE:
			snake.append((next_y, next_x))
			board[next_y][next_x] = SNAKE
		else:
			snake.append((next_y, next_x))
			board[next_y][next_x] = SNAKE
			tail = snake.popleft()
			board[tail[0]][tail[1]] = EMPTY

	return -1

def main():
	global N
	N = int(input())
	K = int(input())
	board = [[EMPTY]*N for _ in range(N)]
	for _ in range(K):
		r, c = map(int, input().strip().split())
		board[r-1][c-1] = APPLE
	L = int(input())

	handling = [input().strip().split() for _ in range(L)]
	handling = dict(handling)
	handling = {int(k):str(v) for k, v in handling.items()}

	end_time = dummy(board, handling)

	print(end_time)
if __name__ == "__main__":
	main()
