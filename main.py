from question_model import question
from data import question_data
from quiz_brain import quizbrain

question_bank=[]

for item in question_data:
    new_text=item['text']
    new_answer=item['answer']
    new_question=question(new_text,new_answer)
    question_bank.append(new_question)

quiz= quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz 😁")
print(f"Your score is {quiz.score}/{quiz.question_number}")