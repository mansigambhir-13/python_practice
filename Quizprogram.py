def run_quiz():
    quiz = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the smallest prime number?": "2",
        "What is the chemical symbol for water?": "H2O",
        "What is 5 multiplied by 6?": "30"
    }

    score = 0
    total_questions = len(quiz)

    print("Welcome to the Quiz!\n")

    for question, correct_answer in quiz.items():
        print(question)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}\n")

    print("Quiz Completed!")
    print(f"Your Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    run_quiz()
# This code defines a simple quiz program that asks the user a series of questions and checks their answers.    