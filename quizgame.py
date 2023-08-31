# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:31:52 2023

@author: Shafeeq
"""
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        
#defining the print statements
    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice questions")
        print()
        print("ARE YOU READY?")
        print()
        print("Let's start!" )
        print()
        print("*Write answer number not the answer*")
        
#asking question
    def ask_question(self, question):
        print(question["question"])
        for index, choice in enumerate(question["choices"], start=1):
            print(f"{index}. {choice}")

#checking if the answer is correct 
    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yayy! Correct Answer !")
            self.score += 1
        else:
            print("Sorry! Incorrect Answer.")
            print("Correct answer is :", correct_answer)

#displaying the final results/scores
    def display_final_results(self):
        print("\nQuiz Finished!")
        print(f"Your score: {self.score}/{len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        if percentage == 100:
            print("Perfect! You're a quiz master!")
        elif percentage >= 70:
            print("Great job! You did well!")
        else:
            print("Do not worry! Keep practicing to improve!")
            
#Questions Asked
def main():
    
    questions = [
      
        {
            "question": "What is 15 + 27?",
            "choices": ["39", "42", "51"],
            "answer": "2"
        },
        {
            "question": "What is the capital of Itlay?",
            "choices": ["Dhaka", "Rome", "London" ],
            "answer": "2"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
            "answer": "1"
        },
        {
            "question": "How many continents are there in the world?",
            "choices": ["10", "8", "7"],
            "answer": "3"
        }
        # Add more questions here
    ]

    quiz = Quiz(questions)
    quiz.display_welcome_message()

    for question in quiz.questions:
        quiz.ask_question(question)
        user_answer = input("Your answer: ")
        quiz.evaluate_answer(user_answer, question["answer"])
        print()

    quiz.display_final_results()

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
