import re
poly = input()
react = re.compile(r'|'.join([c + c.upper() for c in set(poly.lower())] + [c + c.lower() for c in set(poly.upper())]))
while react.search(poly):
    poly = react.sub('', poly)
print(len(poly))
