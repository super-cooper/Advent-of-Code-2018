total = 0
children = []
metadata = []
work_c = 0
work_m = 0
header = 1
for entry in map(int, input().split()):
    if header == 1:
        if work_c > 0:
            children.append(work_c)
        work_c = entry
        header = 2
    elif header == 2:
        if work_m > 0:
            metadata.append(work_m)
        work_m = entry
        header = 0 if work_c == 0 else 1
    else:
        total += entry
        work_m -= 1
        if work_m == 0 and len(metadata) > 0:
            work_m = metadata.pop()
            if work_c == 0:
                work_c = children.pop()
            work_c -= 1
            header = int(work_c > 0)
print(total)
