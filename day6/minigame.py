print("🎉 Welcome to the Python Quiz Game! 🎉")
score = 0

# List of questions and answers
questions = [
    {"question": "What is the keyword to define a function in Python?", "answer": "def"},
    {"question": "Which symbol is used for comments in Python?", "answer": "#"},
    {"question": "What data type is the value: True?", "answer": "bool"},
]

# Loop through questions
for q in questions:
    user_ans = input(q["question"] + " ").lower()
    if user_ans == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

# Final score
print(f"\nYour final score is: {score}/{len(questions)}")

