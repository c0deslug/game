from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank)

newBrain = QuizBrain(question_bank)
print(newBrain)

while newBrain.still_has_questions() is True:
    newBrain.next_question()

print("You've completed the quiz.")
print(f"Your final score was {newBrain.user_score} / {newBrain.question_number}")