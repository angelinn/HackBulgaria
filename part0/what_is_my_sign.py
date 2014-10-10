def what_is_my_sign(day, month):
    months = [
        [20, "Capricorn"],
        [19, "Aquarius"],
        [20, "Pisces"],
        [20, "Aries"],
        [21, "Taurus"],
        [21, "Gemini"],
        [22, "Cancer"],
        [23, "Leo"],
        [23, "Virgo"],
        [23, "Libra"],
        [22, "Scorpio"],
        [21, "Saggitaurus"]
        ]

    if day <= months[month - 1][0]:
        return months[month - 1][1]

    return months[month][1]
