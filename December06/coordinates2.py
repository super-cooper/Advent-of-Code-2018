import sys
from collections import Counter
points = [tuple(map(int, point.split(', '))) for point in sys.stdin.readlines()]
grid = [[-1 for _ in range(max(p[1] for p in points))] for _ in range(max(p[0] for p in points))]
manhattan = lambda a, b: abs(a[1] - b[1]) + abs(a[0] - b[0])
safe = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        tot = sum(manhattan((j, i), p) for p in points)
        if tot < 10_000:
            grid[i][j] = 0
            safe.append((i, j))
region = 1
def search(i, j):
    stack = []
    did_search = False
    if grid[i][j] == 0:
        stack.append((i, j))
        did_search = True
    while len(stack) > 0:
        k, m = stack.pop()
        if grid[k][m] != 0:
            continue
        grid[k][m] = region
        if k + 1 < len(grid):
            stack.append((k + 1, m))
        if k - 1 >= 0:
            stack.append((k - 1, m))
        if m + 1 < len(grid[i]):
            stack.append((k, m + 1))
        if m - 1 >= 0:
            stack.append((k, m - 1))
    return did_search
was_in_region = False
for point in safe:
    searched = search(*point)
    if not searched:
        if was_in_region:
            region += 1
    was_in_region = searched
print(Counter(i for i in sum(grid, []) if i != -1).most_common()[0][1])
