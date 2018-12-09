import re
from collections import defaultdict, deque
circle = deque([0])
info = input()
n_players = int(re.match(r'^([0-9]+).*', info).group(1))
max_marble = int(re.match(r'.+ ([0-9]+) points', info).group(1))
player = 1
scores = defaultdict(int)
for marble in range(1, max_marble):
    if marble % 23 == 0:
        circle.rotate(7)
        scores[player] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
    player = player + 1 if player < n_players else 1
print(max(scores.values()))
