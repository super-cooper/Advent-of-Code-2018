import sys

scan = [line.strip().split(', ') for line in sys.stdin.readlines()]
for i in range(len(scan)):
    prepared = [[scan[i][0][0], scan[i][0][2:]], [scan[i][1][0], scan[i][1][2:]]]
    prepared[0][1] = int(prepared[0][1])
    prepared[1][1] = list(map(int, prepared[1][1].split('..')))
    scan[i] = prepared
left = min(min(line[0][1] for line in scan if line[0][0] == 'x'),
           min(line[1][1][0] for line in scan if line[1][0] == 'x'))
right = max(max(line[0][1] for line in scan if line[0][0] == 'x'),
            max(line[1][1][1] for line in scan if line[1][0] == 'x'))
top = 0
bottom = max(max(line[0][1] for line in scan if line[0][0] == 'y'),
             max(line[1][1][1] for line in scan if line[1][0] == 'y'))
earth = [['.' for _ in range(right + 3)] for _ in range(bottom + 3)]
for i in range(len(scan)):
    clay = [scan[i][0][1], scan[i][1][1][0]] if scan[i][0][0] == 'x' else [scan[i][1][1][0], scan[i][0][1]]
    end = [scan[i][0][1], scan[i][1][1][1] + 1] if scan[i][0][0] == 'x' else [scan[i][1][1][1] + 1, scan[i][0][1]]
    while clay != end:
        earth[clay[1]][clay[0]] = '#'
        if scan[i][0][0] == 'x':
            clay[1] += 1
        else:
            clay[0] += 1
earth[0][500] = '+'
endpoints = [(0, 500)]
while len(endpoints) > 0:
    i, j = endpoints.pop(0)
    if i != bottom and earth[i][j] != '~':
        if earth[i + 1][j] == '.':
            earth[i + 1][j] = '|'
            endpoints.append((i + 1, j))
        elif earth[i + 1][j] in ('~', '#'):
            if all(earth[i][p_j] in ('|', '~', '#') for p_j in [j - 1, j + 1]):
                left_surface, right_surface = j, j
                while earth[i][left_surface] == '|' and left_surface > 0:
                    left_surface -= 1
                while earth[i][right_surface] == '|' and right_surface < len(earth[0]) - 1:
                    right_surface += 1
                if earth[i][left_surface] in ('~', '#') and earth[i][right_surface] in ('~', '#'):
                    earth[i][j] = '~'
                    for p_i, p_j in [(i, j - 1), (i, j + 1), (i - 1, j)]:
                        if earth[p_i][p_j] == '|':
                            endpoints.append((p_i, p_j))
            else:
                for p_j in [j - 1, j + 1]:
                    if earth[i][p_j] == '.':
                        earth[i][p_j] = '|'
                        endpoints.append((i, p_j))
print(sum(sum(c in ('~', '|') for c in row) for row in earth) - 5)
