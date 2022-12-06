
import re
data = open("input.txt")
_PATTERN = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
c=0
for line in data:
        start1, end1, start2, end2 = map(int, re.match(_PATTERN, line).groups())
        if start1 <= end2 and end1 >= start2:
            c += 1

print(c)