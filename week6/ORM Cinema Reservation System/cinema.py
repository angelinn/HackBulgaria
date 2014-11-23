from movie import Movie
from reservation import Reservation
from projection import Projection
from connection import Base, engine
from sqlalchemy.orm import Session

s
class Cinema:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)

    def add_movie(self, name, rating):
        self.session.add(Movie(name=name, rating=rating))
        self.session.commit()

    def add_projection(self, movie_id, type, date, time):
        self.session.add(Projection(movie_id=movie_id, type=type, date=date, time=time))
        self.session.commit()

    def add_reservation(self, username, projection_id, row, col):
        self.session.add(Reservation(username=username, projection_id=projection_id, row=row, col=col))
        self.session.commit()

    def show_movies(self):
        return self.session.query(Movie).all()

    def show_movie_projections(self, movie_id):
        return self.session.query(Projection).filter(Projection.movie_id == movie_id).all()

    def __fill_defaults(self):
        self.add_movie('The Hunger Games: Catching Fire', 7.9)
        self.add_movie('Wreck-It Ralph', 7.8)
        self.add_movie('Her', 8.3)

        self.add_projection(1, '3D', '2014-04-01', '19:10')
        self.add_projection(1, '2D', '2014-04-01', '19:00')
        self.add_projection(1, '4DX', '2014-04-02', '21:00')
        self.add_projection(3, '2D', '2014-04-05', '20:20')
        self.add_projection(2, '3D', '2014-04-02', '22:00')
        self.add_projection(2, '2D', '2014-04-02', '19:30')

        self.add_reservation('RadoRado', 1, 2, 1)
        self.add_reservation('RadoRado', 1, 3, 5)
        self.add_reservation('RadoRado', 1, 7, 8)
        self.add_reservation('Ivo', 3, 1, 1)
        self.add_reservation('Ivo', 3, 1, 2)
        self.add_reservation('Mysterious', 5, 2, 3)
        self.add_reservation('Mysterious', 5, 2, 4)


c = Cinema()
print(c.show_movies())
print(c.show_movie_projections(1))
