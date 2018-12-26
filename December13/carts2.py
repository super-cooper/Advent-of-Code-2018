import sys
from itertools import cycle
track = [list(line) for line in sys.stdin.readlines()]
carts = []
orientation = ('>', '^', '<', 'v')
for i in range(len(track)):
    for j in range(len(track[i])):
        if track[i][j] in '<>':
            carts.append([i, j, orientation.index(track[i][j]), cycle([1, 0, -1])])
            track[i][j] = '-'
        elif track[i][j] in '^v':
            carts.append([i, j, orientation.index(track[i][j]), cycle([1, 0, -1])])
            track[i][j] = '|'
marked = set()
while len(carts) > 1:
    carts.sort(key=lambda c: c[:2])
    for i in range(len(carts)):
        direction = orientation[carts[i][2]]
        if direction == '<':
            carts[i][1] -= 1
        elif direction == '>':
            carts[i][1] += 1
        elif direction == '^':
            carts[i][0] -= 1
        else:
            carts[i][0] += 1
        piece = track[carts[i][0]][carts[i][1]]
        if piece == '/':
            carts[i][2] = (carts[i][2] + (1 if direction == '>' or direction == '<' else -1)) % len(orientation)
        elif piece == '\\':
            carts[i][2] = (carts[i][2] - (1 if direction == '>' or direction == '<' else -1)) % len(orientation)
        elif piece == '+':
            carts[i][2] = (carts[i][2] + next(carts[i][3])) % len(orientation)
        if any((y, x) == tuple(carts[i][:2]) for y, x in [carts[j][:2] for j in range(len(carts)) if j != i]):
            for k in range(len(carts)):
                if carts[k][:2] == carts[i][:2]:
                    marked.add(k)
    carts = [carts[j] for j, _ in enumerate(carts) if j not in marked]
    marked.clear()
print(str(carts.pop()[:2][::-1])[1:-1].replace(' ', ''))
