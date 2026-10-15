import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

records = read_valid(lines)

total = 0
for line in lines:
    if line.strip() != "":
        total += 1
skipped = total - len(records)

avg = average_by_city(records)
best = warmest_city(records)

print(len(records))
print(skipped)
if best == "":
    print("0.0")
else:
    print(f"{avg[best]:.1f}")