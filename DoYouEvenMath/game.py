from user import User
from question import Question
from database_manager import DatabaseManager


class Game:
    DEFAULT_QUESTION_SESSION = 10

    def __init__(self):
        self.manager = DatabaseManager()
        self.user = input('Enter Username: ')

        self.manager.add_user(self.user)
        self.current_question = 1

    def start(self):
        questions_length = self.manager.get_question_count()
        ques = None

        while questions_length > 0:
            ques = self.manager.get_question(self.current_question)
            self.current_question += 1

            print(ques.question)

            answer = input('Get answer: ')

            if ques.answer == int(answer):
                print('Correct!\n')
            else:
                print('Wrong!\n')
                break

            if questions_length == 1:
                for i in range(self.DEFAULT_QUESTION_SESSION):
                    print('Adding more questions!')
                    self.manager.add_random_question()

                questions_length = self.manager.get_question_count()
                print(questions_length)

            questions_length -= 1



Game().start()
