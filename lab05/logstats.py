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
