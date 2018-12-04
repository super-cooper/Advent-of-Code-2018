import sys
import re
from collections import defaultdict
splitter = re.compile(r'\[.+:([0-9]{2})\] (.+)')
guard_getter = re.compile(r'.+ #([0-9]+) .+')
tracker = defaultdict(lambda: defaultdict(int))
guard = None
sleep_start = 0
for t in sorted(sys.stdin.readlines()):
    minute, info = splitter.match(t).group(1, 2)
    if 'G' in info:
        guard = guard_getter.match(info).group(1)
    elif 'fa' in info:
        sleep_start = int(minute)
    else:
        for m in range(sleep_start, int(minute)):
            tracker[guard][m] += 1
worst = max(tracker.keys(), key=lambda g: sum(tracker[g].values()))
print(max(tracker[worst].keys(), key=lambda m: tracker[worst][m]) * int(worst))
