class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.user_score = 0
        self.question_list = qlist

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        curr_q = self.question_list[self.question_number]
        # pulls Question class object from question_list, the model is a class that contains attributes text and answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_q.text} (True/False): ")
        self.check_answer(user_answer, curr_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.user_score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")

