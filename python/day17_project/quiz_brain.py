class QuizBrain:

    def __init__(self, question_list) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        player = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self._check_answer(player, question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def _check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")