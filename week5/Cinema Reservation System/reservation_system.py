import sqlite3


class ReservationSystem:
    def __init__(self):
        self.database = None
        self.cursor = None

        self.create_databases()

    def create_databases(self):
        self.database = sqlite3.connect('movies.db')
        self.cursor = self.database.cursor()

        self.cursor.executemany('PRAGMA foreign_keys=ON')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, date TEXT, time TEXT,
            FOREIGN KEY(movie_id) REFERENCES Movies(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER,
            row INTEGER, col INTEGER, FOREIGN KEY(projection_id) REFERENCES Projections(id))''')

    def fill_movies(self):
        self.add_movie('The Hunger Games: Catching Fire', 7.9)
        self.add_movie('Wreck-It Ralph', 7.8)
        self.add_movie('Her', 8.3)

    def add_movie(self, name, rating):
        self.cursor.execute('INSERT INTO Movies(name, rating) VALUES(?, ?)', (name, rating))
        self.database.commit()

    def remove_movie(self, name):
        self.cursor.execute('DELETE FROM Movies WHERE name = ?', (name,))
        self.database.commit()

    def show_movies(self):
        movies = self.cursor.execute('SELECT * FROM Movies ORDER BY rating DESC')
        for movie in movies:
            print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))

ReservationSystem().show_movies()
