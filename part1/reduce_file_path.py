def reduce_file_path(path):
    splitted = path.split('/')
    result = ""
    print(splitted)

    for i, each in enumerate(splitted):
        if each == '..':
            print("Removing ..")
            del splitted[i - 1]
            del splitted[i]
            print(splitted)

    for each in splitted:
        if each == '':
            result += '/'
        else:
            result += each

    print(result)

reduce_file_path('/etc//wtf/..')
