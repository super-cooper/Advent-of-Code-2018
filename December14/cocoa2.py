import sys
scores, e1, e2 = [3, 7], 0, 1
n, seq = input(), '37'
while True:
    for d in str(scores[e1] + scores[e2]):
        scores.append(int(d))
        seq = seq + d if len(seq) < len(n) else seq[1:] + d
        if seq == n:
            print(len(scores) - len(seq))
            sys.exit()
    e1, e2 = (1 + scores[e1] + e1) % len(scores), (1 + scores[e2] + e2) % len(scores)
