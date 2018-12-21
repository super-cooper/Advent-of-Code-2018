serial = int(input())
grid = {(x, y): ((((((x + 10) * y) + serial) * (x + 10)) // 100) % 10) - 5 for x in range(1, 301) for y in
        range(1, 301)}
power = {(x, y, 1): grid[(x, y)] for x, y in grid}
for x, y in grid:
    for s in range(2, 300):
        if x + s <= 300 and y + s <= 300:
            power[(x, y, s)] = sum(grid[(x + i, y + s - 1)] + grid[(x + s - 1, y + i)] for i in range(s)) + power[
                (x, y, s - 1)]
print(str(max(power, key=lambda p: power[p]))[1:-1].replace(' ', ''))
