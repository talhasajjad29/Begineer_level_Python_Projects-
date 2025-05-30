def display_question(q_data, q_no):
    print(f"\nQ{q_no + 1}: {q_data['question']}")
    for option in q_data["options"]:
        print(option)

def get_user_answer():
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please choose A, B, C, or D.")
        answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer

def check_answer(user_ans, correct_ans):
    return user_ans == correct_ans
def run_quiz():
    quiz = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. JavaScript", "C. HTML", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "What is the output of: 3 * 1 ** 3?",
            "options": ["A. 27", "B. 3", "C. 1", "D. 9"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a Python data type?",
            "options": ["A. set", "B. map", "C. array", "D. tuple"],
            "answer": "D"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Mark Zuckerberg"],
            "answer": "C"
        }
    ]
    score = 0
    print("🎯 Welcome to the Python Quiz App!")
    print("Answer the following questions:\n")
    for i, q in enumerate(quiz):
        display_question(q, i)
        user_ans = get_user_answer()
        if check_answer(user_ans, q["answer"]):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {q['answer']}\n")

    print("🎉 Quiz Completed!")
    print(f"Your Final Score: {score} out of {len(quiz)}")


# Run the Quiz
run_quiz()
