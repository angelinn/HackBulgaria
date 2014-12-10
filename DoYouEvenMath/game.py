from user import User
from question import Question
from database_manager import DatabaseManager


class Game:
    DEFAULT_QUESTION_SESSION = 10

    def __init__(self):
        self.manager = DatabaseManager()
        self.user = None

        self.current_question = 1
        self.question_count = self.manager.get_question_count()

    def show_highscores(self):
        users = self.manager.get_highscores()
        for user in users:
            print('{} - {}'.format(user.name, user.score))

    def add_more_questions(self):
        print('Loading ..\n')
        for i in range(self.DEFAULT_QUESTION_SESSION):
            self.manager.add_random_question()

        self.question_count = self.manager.get_question_count()

    def prompt_user(self):
        self.user = input('Enter Username: ')
        self.manager.add_user(self.user)

    def ask(self):
        self.prompt_user()
        self.add_more_questions()

        ques = None
        score = 0

        while self.question_count > 0:
            ques = self.manager.get_question(self.current_question)
            self.current_question += 1

            print(ques.question)

            answer = input('Get answer: ')

            try:
                if ques.answer == int(answer):
                    print('Correct!\n')
                    score += 2
                else:
                    print('Wrong!\n')
                    break
            except ValueError:
                print('Please enter a valid answer.')
                self.current_question -= 1
                continue

            if self.question_count == 1:
                self.add_more_questions()

            self.question_count -= 1

        self.manager.set_score(self.user, score)

    def start(self):
        while True:
            command = input("> ")
            if command == 'start':
                self.ask()
            elif command == 'highscores':
                self.show_highscores()
            elif command == 'exit':
                return


def main():
    Game().start()

if __name__ == '__main__':
    main()
