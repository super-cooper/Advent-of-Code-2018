import sys
from collections import Counter
twos = 0
threes = 0
for line in sys.stdin.readlines():
    c = Counter(line)
    twos += int(2 in c.values())
    threes += int(3 in c.values())
print(twos * threes)
