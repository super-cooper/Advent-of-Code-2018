import sys
landscape, past = [list(line.strip()) for line in sys.stdin.readlines()], {}
for m in range(1_000_000_000):
    c = str(landscape)
    if c in past:
        for state, minute in past.items():
            if minute == past[c] + (1_000_000_000 - past[c]) % (m - past[c]):
                landscape = eval(state)
                print(sum(a == '#' for a in sum(landscape, [])) * sum(a == '|' for a in sum(landscape, [])))
                sys.exit()
    past[c] = m
    changes = {}
    for i in range(len(landscape)):
        for j in range(len(landscape[i])):
            adj = [(y, x) for y, x in
                   [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i, j + 1), (i - 1, j + 1),
                    (i - 1, j)] if 0 <= y < len(landscape) and 0 <= x < len(landscape[y])]
            if landscape[i][j] == '.' and sum(landscape[y][x] == '|' for y, x in adj) >= 3:
                changes[(i, j)] = '|'
            elif landscape[i][j] == '|' and sum(landscape[y][x] == '#' for y, x in adj) >= 3:
                changes[(i, j)] = '#'
            elif landscape[i][j] == '#' and not all(a in [landscape[y][x] for y, x in adj] for a in ('#', '|')):
                changes[(i, j)] = '.'
    for i, j in changes:
        landscape[i][j] = changes[(i, j)]
