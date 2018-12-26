scores, e1, e2 = [3, 7], 0, 1
n = int(input())
while len(scores) < n + 10:
    scores.extend(map(int, str(scores[e1] + scores[e2])))
    e1, e2 = (1 + scores[e1] + e1) % len(scores), (1 + scores[e2] + e2) % len(scores)
print(''.join(map(str, scores[-10:])))
