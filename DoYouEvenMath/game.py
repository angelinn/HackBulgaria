from user import User
from question import Question
from database_manager import DatabaseManager


class Game:
    def __init__(self):
        manager = DatabaseManager()
        manager.add_user(input('Enter your username: '))

        for i in range(10):
            manager.add_random_question()


Game()
