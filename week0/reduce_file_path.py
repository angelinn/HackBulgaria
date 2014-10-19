def take_out_dots(path):
    i = 0

    while i < len(path):
        if path[i] == '..':
            del path[i]
            del path[i - 1]
            i -= 2

        i += 1


def path_to_string(path):
    result = ""

    for each in path:
        if each != '.':
            result += '/' + each

    return result


def get_max_slashes(path):
    max_slashes = 0
    max_candidate = 0

    for each in path:
        print("Cand {0}, slash {1} ".format(max_candidate, max_slashes))
        if each == '':
            max_candidate += 1
        elif each != '':
            if max_candidate > max_slashes:
                max_slashes = max_candidate
            max_candidate = 0

        if max_candidate > max_slashes:
            max_slashes = max_candidate

    return max_slashes


def reduce_file_path(path):
    splitted = path.split('/')
    result = ""

    take_out_dots(splitted)
    max_slashes = get_max_slashes(splitted)
    print(splitted)

    result = path_to_string(splitted)
    print(max_slashes)
    while max_slashes >= 0:
        result = result.replace('//', '/')
        max_slashes -= 1

    return result

print(reduce_file_path("//////////////"))
