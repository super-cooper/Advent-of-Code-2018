import sys
freq = 0
freqs = set()
inp = [int(x) for x in sys.stdin.readlines()]
while True:
    for x in inp:
        freq += x
        if freq in freqs:
            print(freq)
            sys.exit()
        freqs.add(freq)
