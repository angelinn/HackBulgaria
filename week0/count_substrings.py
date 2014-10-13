def count_substrings(haystack, needle):
    times_met = 0
    index = 0

    for i in range(len(haystack)):
        if haystack.find(needle, index) >= 0:
            times_met += 1
            index = haystack.find(needle, index) + 1
        else:
            break

    return times_met
