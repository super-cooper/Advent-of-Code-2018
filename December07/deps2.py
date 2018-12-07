import string
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
workers = 5
work_time = {c: 60 + (ord(c) - 64) for c in string.ascii_uppercase}
elapsed = 0
working = []
while len(order) < 26:
    while len(ready) > 0 and workers > 0:
        working.append(ready.pop())
        workers -= 1
    for i in range(5 - workers):
        work_time[working[i]] -= 1
    elapsed += 1
    for task in [proc for proc in working if work_time[proc] == 0]:
        working.remove(task)
        workers += 1
        order.append(task)
        ready += [step for step in deps if all(dep in order for dep in deps[step])]
        ready.sort(reverse=True)
        for step in ready:
            if step in deps:
                del deps[step]
print(elapsed)
