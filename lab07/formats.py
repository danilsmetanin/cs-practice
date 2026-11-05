import json


def csv_to_records(text):
    if not text:
        return []

    lines = [line for line in text.splitlines() if line.strip() != ""]
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        record = {}
        for i in range(len(headers)):
            record[headers[i]] = parts[i] if i < len(parts) else ""
        records.append(record)

    return records


def to_value(value):
    low = value.lower()

    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        return value


def parse_settings(lines):
    result = {}
    list_key = None

    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if line == "":
            continue

        if line.startswith("-"):
            item = line[1:].strip()
            if list_key is not None:
                result[list_key].append(to_value(item))
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value == "":
            result[key] = []
            list_key = key
        else:
            result[key] = to_value(value)
            list_key = None

    return result


def merge_by_key(rows, extra, key="id"):
    result = []

    for row in rows:
        k = row.get(key)
        add = extra.get(k, {})

        new_row = {}
        for a in add:
            new_row[a] = add[a]
        for a in row:
            new_row[a] = row[a]

        result.append(new_row)

    return result


def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)