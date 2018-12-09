def score(arr):
    scores = []
    children, meta = arr[:2]
    arr = arr[2:]
    for _ in range(children):
        x, arr = score(arr)
        scores.append(x)
    if children == 0:
        return sum(arr[:meta]), arr[meta:]
    else:
        return sum(scores[i - 1] for i in arr[:meta] if 0 < i <= len(scores)), arr[meta:]
print(score([int(x) for x in input().split()])[0])
