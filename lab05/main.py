import sys
from logstats import parse_event, count_levels, top_errors, format_report

path = sys.stdin.readline().strip()

total = 0
errors = 0
broken = 0

with open(path, encoding="utf-8") as log:
    for line in log:
        if line.strip() == "":
            continue
        total += 1
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                errors += 1
        except ValueError:
            broken += 1

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(path, encoding="utf-8") as log:
    top = top_errors(log, 3)

report = format_report(counts, top)

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print(total)
print(errors)
print(broken)