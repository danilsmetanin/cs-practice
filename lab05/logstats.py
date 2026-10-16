LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]


def parse_event(line):
    parts = line.strip().split(" ", 2)
    if len(parts) != 3:
        raise ValueError("не три части")
    time = parts[0]
    level = parts[1]
    message = parts[2].strip()
    if time == "":
        raise ValueError("пустое время")
    if level not in LEVELS:
        raise ValueError("незнакомый уровень")
    if message == "":
        raise ValueError("пустое сообщение")
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
    messages = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            messages[msg] = messages.get(msg, 0) + 1
    pairs = []
    for msg in messages:
        pairs.append([msg, messages[msg]])
    pairs.sort(key=lambda p: (-p[1], p[0]))
    return pairs[:n]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        text += level + ": " + str(counts[level]) + "\n"
    text += "\nЧастые ошибки:\n"
    for pair in errors:
        text += "- " + pair[0] + " — " + str(pair[1]) + "\n"
    return text