import os

from logstats import count_levels, format_report, top_errors

filename = input().strip()

with open(filename, encoding="utf-8") as log:
    counts = count_levels(log)

with open(filename, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

report = format_report(counts, errors)
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.txt")

with open(report_path, "w", encoding="utf-8", newline="\n") as file:
    file.write(report)
