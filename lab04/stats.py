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
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("температура не число")
    return {"city": city, "temperature": temperature, "date": date}