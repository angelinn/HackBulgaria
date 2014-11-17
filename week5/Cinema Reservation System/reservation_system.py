from copy import deepcopy
from seat import Seat
from database_manager import DatabaseManager


class ReservationSystem:
    MAX_SEATS = 100
    LENGTH = 10
    WIDTH = 10
    __TOP_CINEMA_SEATS = '   1 2 3 4 5 6 7 8 9 10'

    def __init__(self):
        self.manager = DatabaseManager()
        self.manager.create_databases()

        self.cinema_hall = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

    def show_movies(self):
        movies = self.manager.cursor.execute('SELECT * FROM Movies ORDER BY rating DESC')

        for movie in movies:
            print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))

    def make_reservation(self):
        name = input('Input name > ')
        tickets = int(input('Number of tickets > '))

        print('Current Movies: ')
        self.show_movies()

        choice = input('Choose a movie > ')
        movie_name = self.manager.cursor.execute('''SELECT name
                                                    FROM Movies
                                                    WHERE ? = id''', (choice,)).fetchone()[0]
        self.list_projections(movie_name, choice)

        projection_choice = input('Choose projection > ')
        hall_map = self.list_available_seat_map(projection_choice)

        seats = self.choose_seats(hall_map, tickets)

        date = self.manager.cursor.execute('''SELECT date, time
                                      FROM Projections
                                      WHERE id = ?''', (projection_choice, )).fetchone()

        seats_string = ''
        for seat in seats:
            seats_string += '{} '.format(str(seat))

        self.summit_reservation(name, movie_name, '{} {}'.format(date[0], date[1]), seats_string)

        finalizer = input('Write "finalize" to confirm > ')
        if finalizer == 'finalize':
            for seat in seats:
                self.add_reservation(name, projection_choice, seat[0], seat[1])

    def summit_reservation(self, name, movie_name, date, seats):
        print('This is your reservation:\nMovie: {}\nDate: {}\nSeats: {}\n\n'
              .format(movie_name, date, seats))

    def choose_seats(self, hall_map, tickets_count):
        result = []

        while tickets_count > 0:
            seat_choice_string = tuple(input("Choose a seat (e.g '(1, 2)') > "))
            seat_choice = Seat.string_to_seat_tuple(seat_choice_string)

            if Seat.isOutOfRange(seat_choice[0], seat_choice[1], self.LENGTH, self.WIDTH) is True:
                print("Seat is out of boundries")

            elif hall_map[seat_choice[0] - 1][seat_choice[1] - 1] == Seat.SEAT_TAKEN:
                print("Seat is already taken")
            else:
                result.append(seat_choice)
                tickets_count -= 1

        return result

    def list_projections(self, movie_name, choice):
        print('Projections for {}: '.format(movie_name))
        projections = self.manager.cursor.execute('''SELECT id, date, time, type
                                                     FROM Projections
                                                     WHERE movie_id = ?''', (choice, )).fetchall()

        for proj in projections:
            slots = self.manager.cursor.execute('''SELECT Projections.id
                                           FROM Projections
                                           INNER JOIN Reservations
                                           ON Projections.id = Reservations.projection_id
                                           WHERE Projections.id = ?''', (proj[0], ))

            print('[{}] - {} {} ({}) - {}  seats available'.format
                 (proj[0], proj[1], proj[2], proj[3], self.MAX_SEATS - len(list(slots))))

        return projections

    def list_available_seat_map(self, projection_choice):
        print('Available seats (marked with a dot):')

        matrix = deepcopy(self.cinema_hall)
        occupied = self.manager.cursor.execute('''SELECT Reservations.row, Reservations.col
                                          FROM Reservations
                                          INNER JOIN Projections
                                          ON Reservations.projection_id = Projections.id
                                          WHERE Projections.id = ?''', (projection_choice, ))

        for seat in occupied:
            matrix[seat[0] - 1][seat[1] - 1] = Seat.SEAT_TAKEN

        row = ''

        print(self.__TOP_CINEMA_SEATS)

        for i in range(10):
            row += '{:2} '.format(i + 1)

            for j in range(10):
                row += '{} '.format(matrix[i][j])

            print(row)
            row = ''

        return matrix
    #def go(self):


ReservationSystem().make_reservation()
