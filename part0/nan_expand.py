def nan_expand(n):
    if n == 0:
        return ""
    if n == 1:
        return "Not a NaN"

    return "Not a " + nan_expand(n - 1)