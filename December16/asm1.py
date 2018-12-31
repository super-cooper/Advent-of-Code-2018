import sys
info, count, i = [row.strip() for row in sys.stdin.readlines()], 0, 0
ops = [
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] + regs[b] for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] + b for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] * regs[b] for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] * b for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] & regs[b] for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] & b for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] | regs[b] for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] | b for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else regs[a] for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else a for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if a > regs[b] else 0) for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if regs[a] > b else 0) for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if regs[a] > regs[b] else 0) for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if a == regs[b] else 0) for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if regs[a] == b else 0) for r in range(len(regs))],
    lambda a, b, c, regs: [regs[r] if r != c else (1 if regs[a] == regs[b] else 0) for r in range(len(regs))],
]
while info[i] != '':
    before = eval(info[i][len('Before '):])
    after = eval(info[i + 2][len('After '):])
    instr = list(map(int, info[i + 1].split()))
    count += len([op for op in ops if op(*instr[1:], before) == after]) >= 3
    i += 4
print(count)
