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
asm = [set(range(16)) for _ in range(16)]
while info[i] != '':
    before = eval(info[i][len('Before '):])
    after = eval(info[i + 2][len('After '):])
    instr = list(map(int, info[i + 1].split()))
    asm[instr[0]].intersection_update(o for o, op in enumerate(ops) if op(*instr[1:], before) == after)
    i += 4
while any(len(instr) > 1 for instr in asm):
    solved = [list(instr)[0] for instr in asm if len(instr) == 1]
    for j in range(len(asm)):
        if len(asm[j]) > 1:
            asm[j].difference_update(solved)
asm, reg = [ops[s.pop()] for s in asm], [0] * 4
for j in range(i + 3, len(info)):
    instr = list(map(int, info[j].split()))
    reg = asm[instr[0]](*instr[1:], reg)
print(reg[0])
