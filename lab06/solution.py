import os


def count_by_extension(paths):
    result = {}

    for path in paths:
        name = os.path.basename(path)
        ext = os.path.splitext(name)[1]  # например, ".PDF" или ""
        ext = ext[1:].lower()            # убираем точку и делаем нижний регистр

        if ext in result:
            result[ext] += 1
        else:
            result[ext] = 1

    return result


def deepest_path(paths):
    if not paths:
        return ""

    best = paths[0]
    best_depth = best.count("/")

    for path in paths[1:]:
        depth = path.count("/")

        if depth > best_depth:
            best = path
            best_depth = depth
        elif depth == best_depth and path < best:
            best = path

    return best


