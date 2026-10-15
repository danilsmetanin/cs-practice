def parse_record(line):
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("не три поля")
    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()
    if city == "":
        raise ValueError("пустой город")
    if date == "":
        raise ValueError("пустая дата")
    temp = temp.replace(",", ".")
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("температура не число")
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines):
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            pass
    return records


def average_by_city(records):
    total = {}
    count = {}
    for r in records:
        city = r["city"]
        total[city] = total.get(city, 0) + r["temperature"]
        count[city] = count.get(city, 0) + 1
    result = {}
    for city in total:
        result[city] = round(total[city] / count[city], 1)
    return result


def warmest_city(records):
    avg = average_by_city(records)
    if len(avg) == 0:
        return ""
    best = ""
    for city in avg:
        if best == "":
            best = city
        elif avg[city] > avg[best]:
            best = city
        elif avg[city] == avg[best] and city < best:
            best = city
    return best