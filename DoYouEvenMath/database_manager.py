from user import User
from question import Question
from connection import Base, engine
from sqlalchemy.orm import Session
from random_operation import RandomOperation
from random import randint


class DatabaseManager:
    QUESTION_PREFIX = 'What is the answer of {} {} {}'

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)

    def __del__(self):
        self.session.query(Question).delete()
        self.session.commit()

    def add_question_console(self):
        ques = input('Enter the question: ')
        answ = input('Enter the answer: ')

        self.session.add(Question(question=ques, answer=answ))
        self.session.commit()

    def add_random_question(self):
        oper = RandomOperation(randint(0, 20), randint(0, 20))
        oper.do_real_operation()

        self.session.add(Question(question=self.QUESTION_PREFIX.format(oper.a, oper.sign, oper.b),
                                  answer=oper.result))
        self.session.commit()

    def add_user(self, name):
        try:
            self.session.query(User).filter(User.name == name).one()

        except Exception:
            self.session.add(User(name=name, score=-1))
            self.session.commit()

    def set_score(self, user, score):
        if score > self.session.query(User).filter(User.name == user).one().score:
            self.session.query(User).filter(User.name == user).update({'score': score})
            self.session.commit()

    def get_question_count(self):
        return self.session.query(Question).count()

    def get_question(self, number):
        return self.session.query(Question).filter(Question.id == number).one()

    def get_highscores(self):
        return self.session.query(User).all()
