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
while True:
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
            print(str(carts[i][:2][::-1])[1:-1].replace(' ', ''))
            sys.exit()
