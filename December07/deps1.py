import sys
import re
from collections import defaultdict
split = re.compile(r'Step ([A-Z]) .+ step ([A-Z]) .+')
steps = [tuple(split.match(line).group(1, 2)) for line in sys.stdin.readlines()]
deps = defaultdict(list)
for step in steps:
    deps[step[1]].append(step[0])
ready = sorted([c for c in set(sum(deps.values(), [])) if c not in deps], reverse=True)
order = []
while len(order) < 26:
    step = ready.pop()
    order.append(step)
    ready += [task for task in deps if all(dep in order for dep in deps[task])]
    ready.sort(reverse=True)
    for task in ready:
        if task in deps:
            del deps[task]
print(''.join(order))
