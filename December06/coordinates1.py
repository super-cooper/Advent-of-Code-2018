import sys
from collections import Counter
points = [tuple(map(int, point.split(', '))) for point in sys.stdin.readlines()]
grid = [[-1 for _ in range(max(p[1] for p in points))] for _ in range(max(p[0] for p in points))]
manhattan = lambda a, b: abs(a[1] - b[1]) + abs(a[0] - b[0])
inf = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        closest = min(manhattan((j, i), p) for p in points)
        all_closest = [p for p in points if manhattan((j, i), p) == closest]
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[i]) - 1:
            for p in all_closest:
                inf.add(p)
        if len(all_closest) == 1 and all_closest[0] not in inf:
            grid[i][j] = points.index(all_closest[0])
print(Counter(i for i in sum(grid, []) if i != -1).most_common()[0][1])
