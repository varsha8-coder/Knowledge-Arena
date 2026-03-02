def quiz_game():
    questions = [
        {
            "question": "1. Which is the largest planet in our Solar System?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "2. Who is known as the Father of the Nation in India?",
            "options": ["A) Jawaharlal Nehru", "B) Subhas Chandra Bose", "C) Mahatma Gandhi", "D) Bhagat Singh"],
            "answer": "C"
        },
        {
            "question": "3. Which is the longest river in the world?",
            "options": ["A) Amazon River", "B) Nile River", "C) Ganga River", "D) Yangtze River"],
            "answer": "B"
        },
        {
            "question": "4. Which desert is the largest hot desert in the world?",
            "options": ["A)Arabian Desert", "B) Gobi desert", "C)Sahara desert","D) Thar desert"],
            "answer": "C"
        },
        {
            "question": "5. What is the national currency of Japan?",
            "options": ["A) Dollar", "B) Yen", "C) Peso", "D) Euro"],
            "answer": "B"
        }
    ]
    score = 0
    print("Welcome to the General Knowledge Quiz!")
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is", q["answer"])
    print("Quiz Completed!")
    print("Your final score is:", score, "/", len(questions))
    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")
    if percentage >= 80:
        print("Excellent Performance!")
    elif percentage >= 50:
        print("Good Job")
    else:
        print("Keep Practicing")
quiz_game()
