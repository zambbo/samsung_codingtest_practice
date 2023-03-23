from collections import deque
import copy

DIRECT = ["N", "W", "S", "E"]

def get_next_direct(di: str) -> list[str]:
	next_direct = []
	if di == "N" or di == "S":
		next_direct = ["W", "E"]
	else:
		next_direct = ["S", "N"]
	return next_direct

def move(board: list[list[chr]], r_idx: list[int], b_idx: list[int], direct: str) -> (list[list[chr]], list[int], list[int]):
	first_move = copy.deepcopy(b_idx)
	second_move = copy.deepcopy(r_idx)
	dy, dx = 0, 0 
	if direct == "N":
		first_move, second_move = (copy.deepcopy(b_idx), copy.deepcopy(r_idx)) if b_idx[0] < r_idx[0] else (copy.deepcopy(r_idx), copy.deepcopy(b_idx))
		dy, dx = -1, 0
	elif direct == "W":
		first_move, second_move = (copy.deepcopy(b_idx), copy.deepcopy(r_idx)) if b_idx[1] < r_idx[1] else (copy.deepcopy(r_idx), copy.deepcopy(b_idx)) 
		dy, dx = 0, -1
	elif direct == "S":
		first_move, second_move = (copy.deepcopy(b_idx), copy.deepcopy(r_idx)) if b_idx[0] > r_idx[0] else (copy.deepcopy(r_idx), copy.deepcopy(b_idx))
		dy, dx = 1, 0
	elif direct == "E":
		first_move, second_move = (copy.deepcopy(b_idx), copy.deepcopy(r_idx)) if b_idx[1] > r_idx[1] else (copy.deepcopy(r_idx), copy.deepcopy(b_idx))
		dy, dx = 0, 1
	else:
		pass
	first_move_origin = copy.deepcopy(first_move)
	second_move_origin = copy.deepcopy(second_move)
	first_color, second_color = (board[first_move_origin[0]][first_move_origin[1]], board[second_move_origin[0]][second_move_origin[1]])
	
	while board[first_move[0] + dy][first_move[1] + dx] != "#":
		if board[first_move[0]][first_move[1]] == "O":
			break

		first_move[0] += dy
		first_move[1] += dx

	board[first_move_origin[0]][first_move_origin[1]] = "."
	board[first_move[0]][first_move[1]] = first_color if board[first_move[0]][first_move[1]] == "." else board[first_move[0]][first_move[1]]
	
	while board[second_move[0] + dy][second_move[1] + dx] != "#" and board[second_move[0] + dy][second_move[1] + dx] != first_color:
		if board[second_move[0]][second_move[1]] == "O":
			break

		second_move[0] += dy
		second_move[1] += dx
	
	board[second_move_origin[0]][second_move_origin[1]] = "."
	board[second_move[0]][second_move[1]] = second_color if board[second_move[0]][second_move[1]] == "." else board[second_move[0]][second_move[1]]
	red_idx, blue_idx = (copy.deepcopy(first_move), copy.deepcopy(second_move)) if first_color == "R" else (copy.deepcopy(second_move), copy.deepcopy(first_move))
	return board, red_idx, blue_idx


def bfs(board: list[list[chr]], r_idx: list[int], b_idx: list[int], o_idx: list[int]) -> int:
	cnt = 0

	queue = deque()

	queue.append((board, r_idx, b_idx, cnt, DIRECT))

	while queue:
		cur_board, cur_r_idx, cur_b_idx, cnt, next_direct = queue.popleft()
		if cnt >= 10:
			return -1
		
		for di in next_direct:
			next_board, next_r_idx, next_b_idx = move(copy.deepcopy(cur_board), cur_r_idx, cur_b_idx, di)
			if next_b_idx == o_idx:
				pass
			elif next_r_idx == o_idx:
				return cnt+1
			elif board == next_board:
				pass
			else:
				queue.append((next_board, next_r_idx, next_b_idx, cnt+1, get_next_direct(di)))
		

	return -1
		

def main():
	N, M = map(int, input().split())
	board = [list(input().strip()) for _ in range(N)]
	r_idx, b_idx, o_idx = ([0]*2, [0]*2, [0]*2)	

	for i in range(N):
		for j in range(M):
			if board[i][j] == "R":
				r_idx = [i, j]
			elif board[i][j] == "B":
				b_idx = [i, j]
			elif board[i][j] == "O":
				o_idx = [i, j]

	cnt = bfs(board, r_idx, b_idx, o_idx)
	
	print(cnt)

if __name__ == "__main__":
	main()
