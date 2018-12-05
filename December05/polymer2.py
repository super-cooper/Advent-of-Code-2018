import re
poly = input()
react = re.compile(r'|'.join([c + c.upper() for c in set(poly.lower())] + [c + c.lower() for c in set(poly.upper())]))
def reduce(strand):
    while react.search(strand):
        strand = react.sub('', strand)
    return strand
print(min(len(reduce(poly.replace(c, '').replace(c.upper(), ''))) for c in set(poly.lower())))
