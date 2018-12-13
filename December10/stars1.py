import sys
import re
pos = re.compile(r'position=<((\s+)?-?[0-9]+),((\s+)?-?[0-9]+)>.+')
velo = re.compile(r'.*velocity=<((\s+)?-?[0-9]+),((\s+)?-?[0-9]+)>')
data = [list(map(int, pos.match(point).group(1, 3))) + list(map(int, velo.match(point).group(1, 3))) for point in
        sys.stdin.readlines()]
grid = [[' ' for _ in range(500)] for _ in range(len(data))]
iterations = min(enumerate(max(x + i * vx for (x, _, vx, __) in data) - min(x + i * vx for (x, _, vx, __) in data)
                 + max(y + i * vy for (_, y, __, vy) in data) - min(y + i * vy for (_, y, __, vy) in data) for i in
                 range(50_000)), key=lambda x: x[1])[0]
for (x, y, vx, vy) in data:
    grid[y + iterations * vy][x + iterations * vx] = '*'
print('\n'.join(''.join(line).lstrip() for line in grid if not all(c == ' ' for c in line)))
