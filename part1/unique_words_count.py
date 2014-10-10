from count_words import count_words


def unique_words_count(arr):
    words = count_words(arr)
    unique_count = 0

    for each in words:
        if words[each] == 1:
            unique_count += 1

    return unique_count

print(unique_words_count)
