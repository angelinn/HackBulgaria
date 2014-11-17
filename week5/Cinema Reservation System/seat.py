class Seat:
    SEAT_TAKEN = 'X'

    @staticmethod
    def string_to_seat_tuple(string):
        x = 0
        y = 0

        done = False

        for char in string:
            if char >= '0' and char <= '9':
                if done is False:
                    done = True
                    x = int(char)
                else:
                    y = int(char)

        if done is False:
            raise ValueError

        return (x, y)

    @staticmethod
    def isOutOfRange(x, y, x_limiter, y_limiter):
        if x < 1 or x > x_limiter or y < 1 or y > y_limiter:
            return True

        return False
