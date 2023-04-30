class QuizBrain:
    def __init__(self, q_list: list) -> None:
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self) -> str:
        if self.q_number < len(self.q_list):
            ans = input(
                f"Q.{self.q_number+1}: {self.q_list[self.q_number].text} (True/False)?: ")
            self.q_number += 1
            return ans

    def still_has_question(self) -> bool:
        return self.q_number < len(self.q_list)

    def user_exp(self, finish: bool):
        print("That's wrong." if finish else "You got it right!")
        print(
            f"The correct answer was: {self.q_list[self.q_number - 1].answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}.")

    def check_answer(self, answer: str):
        if answer == self.q_list[self.q_number - 1].answer:
            self.score += 1
            self.user_exp(False)
        else:
            self.user_exp(True)
            return False
