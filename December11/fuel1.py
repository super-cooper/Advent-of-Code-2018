serial = int(input())
grid = {(x, y): ((((((x + 10) * y) + serial) * (x + 10)) // 100) % 10) - 5 for x in range(1, 301) for y in range(1, 301)}
print(str(max((p for p in grid if p[0] < 299 and p[1] < 299),
              key=lambda p: sum(grid[(p[0] + i, p[1] + j)] for i in range(3) for j in range(3))))[1:-1].replace(' ',
                                                                                                                ''))
