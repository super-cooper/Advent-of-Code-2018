import re
import sys
from collections import defaultdict

splitter = re.compile('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')
claims = [list(map(int, splitter.match(line).group(1, 2, 3, 4, 5))) for line in sys.stdin.readlines()]
inches = defaultdict(int)
for claim in claims:
    for inch in ((x, y) for x in range(claim[1], claim[1] + claim[3]) for y in range(claim[2], claim[2] + claim[4])):
        inches[inch] += 1
for claim in claims:
    if all(inches[inch] == 1 for inch in
           ((x, y) for x in range(claim[1], claim[1] + claim[3]) for y in range(claim[2], claim[2] + claim[4]))):
        print(claim[0])
        sys.exit()
