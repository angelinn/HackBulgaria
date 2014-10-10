def group_by(function, seq):

    result = {}

    for each in seq:
        key = function(each)

        if key in result:
            result[key].append(each)
        else:
            result[key] = [each]

    return result
