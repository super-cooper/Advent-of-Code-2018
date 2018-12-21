import sys
from collections import defaultdict
notes = sys.stdin.readlines()
plants = defaultdict(lambda: '.', {i: state for i, state in enumerate(notes[0].replace('initial state: ', '').strip())})
leftmost, rightmost = 0, len(plants) - 1
notes = {state: instruction for state, instruction in (note.strip().split(' => ') for note in notes[2:])}
for g in range(1, 50_000_000_001):
    changes = set()
    pot = leftmost
    old = ''.join(plants[i] for i in sorted(plants.keys())).lstrip('.')
    while pot <= rightmost:
        group = ''.join(plants[i] if i in plants else '.' for i in range(pot - 2, pot + 3))
        changes.add((pot, notes[group]))
        leftmost = min(leftmost, pot - 2 if notes[group] == '#' else leftmost)
        rightmost = max(rightmost, pot + 2 if notes[group] == '#' else rightmost)
        pot += 1
    plants.update({change[0]: change[1] for change in changes})
    if ''.join(plants[i] for i in sorted(plants.keys())).lstrip('.') == old:
        print(sum(pot + 50_000_000_000 - g for pot in plants if plants[pot] == '#'))
        break
