import sys
from collections import OrderedDict

board = [list(row.strip()) for row in sys.stdin.readlines()]
hp = {(i, j): 200 for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == 'E' or board[i][j] == 'G'}
targets, rounds = [], 0


def bfs(i, j, k, m):
    visited, work = OrderedDict({(a, b): False for a in range(len(board)) for b in range(len(board[a]))}), [(i, j)]
    prev = {}
    visited[(i, j)] = True
    while len(work) != 0:
        y, x = work.pop(0)
        for a, b in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
            if (a, b) in visited and not visited[(a, b)] and board[a][b] != '#':
                prev[(a, b)] = (y, x)
                if (a, b) == (k, m):
                    path = [(a, b)]
                    while (a, b) in prev:
                        path.append(prev[(a, b)])
                        a, b = prev[(a, b)]
                    return list(reversed(path[:-1]))
                if board[a][b] not in ('G', 'E'):
                    visited[(a, b)] = True
                    work.append((a, b))
    return [(-1, -1)] * (len(board) * len(board[0]) + 1)


while True:
    targets = set()
    for i, j in sorted((k, m) for m in range(len(board[0])) for k in range(len(board)) if board[k][m] in ('E', 'G')):
        if board[i][j] == 'E':
            targets = sorted({(k, m) for m in range(len(board[0])) for k in range(len(board)) if board[k][m] == 'G'})
        elif board[i][j] == 'G':
            targets = sorted({(k, m) for m in range(len(board[0])) for k in range(len(board)) if board[k][m] == 'E'})
        else:
            continue
        if len(targets) == 0:
            print(rounds * sum(
                hp[(i, j)] for j in range(len(board[0])) for i in range(len(board)) if board[i][j] in ('G', 'E')))
            sys.exit()
        m_i, m_j = min([bfs(i, j, *target) for target in targets], key=lambda path: len(path))[0]
        if (m_i, m_j) != (-1, -1) and board[m_i][m_j] not in ('G', 'E'):
            board[m_i][m_j] = board[i][j]
            board[i][j] = '.'
            hp[(m_i, m_j)] = hp[(i, j)]
            del hp[(i, j)]
            targets = set()
            i, j = m_i, m_j
        adj = [(y, x) for y, x in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)) if
               board[y][x] in ('G', 'E') and board[y][x] != board[i][j]]
        if len(adj) > 0:
            victim = min(adj, key=lambda x: hp[x])
            hp[victim] -= 3
            if hp[victim] <= 0:
                board[victim[0]][victim[1]] = '.'
                del hp[victim]
    rounds += 1
