from collections import deque

N = 0
M = 0
K = 0


dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def autumnNsummer(trees: list[list], ground: list[list[int]]) -> None:
    global N
    
    for i in range(N):
        for j in range(N):
            cur_food = ground[i][j]

            new_tree = deque()
            ground[i][j] = 0
            while trees[i][j]:
                cur_tree = trees[i][j].popleft()
             
                if cur_food < cur_tree:
                    ground[i][j] += cur_tree // 2
                else:
                    cur_food -= cur_tree
                    new_tree.append(cur_tree + 1)
            ground[i][j] += cur_food

            trees[i][j] = new_tree

def fallNwinter(trees: list[list], ground: list[list[int]], foods: list[list[int]]) -> None:
    global N

    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree % 5 != 0: continue
                for dyy, dxx in zip(dy, dx):
                    adj_y = i + dyy
                    adj_x = j + dxx
                    if adj_y >=0 and adj_y < N and adj_x >= 0 and adj_x < N:
                        trees[adj_y][adj_x].appendleft(1)

            ground[i][j] += foods[i][j]

def get_alive_tree(trees: list[list]) -> None:
    tree_sum = 0

    for line in trees:
        for tree in line:
            tree_sum += len(tree)

    return tree_sum


def main():
    global N, M, K

    N, M, K = map(int, input().strip().split())
    
    ground = [[5] * N for _ in range(N)]

    trees = [[deque() for _ in range(N)]  for _ in range(N)]
    

    foods = [list(map(int, input().strip().split())) for _ in range(N)]
    
    for _ in range(M):
        r, c, age = map(int, input().strip().split())
        trees[r-1][c-1].append(age)
    
    for _ in range(K):
        autumnNsummer(trees, ground)
        fallNwinter(trees, ground, foods)
    
    tree_sum = get_alive_tree(trees)
    print(tree_sum)



if __name__ == "__main__":
    main()
