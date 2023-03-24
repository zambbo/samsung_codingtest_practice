import copy

N = 0
MAX_VALUE = 0

west_to_west = lambda l: l #기준
north_to_west = lambda l: [list(ll) for ll in list(zip(*l))]
east_to_west = lambda l: [ll[::-1] for ll in l]
south_to_west = lambda l: [list(ll) for ll in list(zip(*l[::-1]))]

ROTATE_FUNCS = [north_to_west, west_to_west, east_to_west, south_to_west]

def move_west(board: list[list[int]]) -> list[list[int]]:
	global N
	
	for line in board:
		maximum = 0
		for i in range(1, N, 1):
			if line[i] == 0: continue #이놈때문에 3시간 녹임
			for j in range(i, maximum, -1):
				if line[j-1] == line[j]: # collision
					line[j-1] *= 2
					line[j] = 0
					maximum = j
					break
				elif line[j-1] == 0: # move
					line[j-1] = line[j]
					line[j] = 0
				else: #greater or smaller
					maximum = j-1
					break
		
	return board

def dfs(board: list[list[int]], depth:int) -> None:
	if depth > 5:
		return

	global MAX_VALUE

	if depth == 5:
		cur_max = max(map(max, board)) # 원래 max(max(board))로 짰음 ㅋㅋ
		MAX_VALUE = max(cur_max, MAX_VALUE)
		return

	for rotate_func in ROTATE_FUNCS:
		cur_board = copy.deepcopy(board)
		cur_board = rotate_func(cur_board)
		cur_board = move_west(cur_board)
		
		#if rotate_func(board) != cur_board: #promising #얘가 문제였음
		dfs(cur_board, depth + 1) 					


def main():
	global N
	global MAX_VALUE

	N = int(input())
	board = [list(map(int, input().strip().split())) for _ in range(N)]

	if N > 1: #얘로 2시간 더 날림
		dfs(board, 0)
	else:
		MAX_VALUE = board[0][0]
	print(MAX_VALUE)

if __name__ == "__main__":
	main()
