import sys
boxes = sys.stdin.readlines()
for b1 in boxes:
    for b2 in boxes:
        for i in range(len(b1)):
            if sum(b1[i] != b2[i] for i in range(len(b1))) == 1:
                print(''.join(b1[i] if b1[i] == b2[i] else '' for i in range(len(b1))))
                sys.exit()
