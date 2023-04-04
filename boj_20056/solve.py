

N, M, K = map(int, input().split())
board = [[0]*N for _ in range(N)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

fireballs = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())

    fireballs.append((r-1,c-1,m,s,d))


def splitted(fireball_dict: dict):
    global fireballs

    fireballs = []
    for key, value in fireball_dict.items():
        if len(value) == 1:
            fireballs.append((*key, *value[0]))
        else:
            combined_m = sum(v[0] for v in value) // 5
            combined_v = sum(v[1] for v in value) // len(value)

            if combined_m == 0: continue

            if all(v[2] % 2 == 0 for v in value) or all(v[2] % 2 == 1 for v in value):
                for d in [0, 2, 4, 6]:
                    fireballs.append((*key, combined_m, combined_v, d))
            else:
                for d in [1, 3, 5, 7]:
                    fireballs.append((*key, combined_m, combined_v, d))
def move():
    fireball_dict = dict()

    for r, c, m, s, d in fireballs:
        ddy = dy[d]
        ddx = dx[d]
        n_r = (r + ddy * s) % N
        n_c = (c + ddx * s) % N

        if (n_r, n_c) not in fireball_dict:
            fireball_dict[(n_r, n_c)] = [(m, s, d)]
        else:
            fireball_dict[(n_r, n_c)].append((m, s, d))

    splitted(fireball_dict)


for _ in range(K):
    move()

print(sum(f[2] for f in fireballs))





