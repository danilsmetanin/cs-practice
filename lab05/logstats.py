LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("bad line")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError("bad level")
    if message == "":
        raise ValueError("bad message")

    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"

        counts[level] = counts.get(level, 0) + 1

    return counts


def top_errors(lines, n):
    counts = {}
    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            counts[message] = counts.get(message, 0) + 1

    result = []
    for message in counts:
        result.append([message, counts[message]])

    result.sort(key=lambda pair: (-pair[1], pair[0]))
    return result[:n]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        text += f"{level}: {counts[level]}\n"

    text += "\nЧастые ошибки:\n"
    for message, count in errors:
        text += f"- {message} — {count}\n"

    return text
