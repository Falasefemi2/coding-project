def quiz_app(): 
    quiz_question = [
        {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kaduna"], "answer": "Abuja"},
        {"question": "Who won Nigeria new presidential election?", "options": ["Peter Obi", "Barrak Obama", "Bola Tinubu"], "answer": "Bola Tinubu"},
        {"question": "Which team has won the league 4x in a row in england?", "options": ["Manchester city", "Arsenal", "London club"], "answer": "Manchester city"},
        {"question": "Who sang not like us?", "options": ["Lamar", "Wizkid", "Brown"], "answer": "Lamar"},
    ]
    
    score = 0
    
    for i, q in enumerate(quiz_question, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        
        while True:
            user_input = input("Enter your choice: ").strip()
            if user_input.isdigit() and 1 <= int(user_input) <= len(q["options"]):
                user_choice = q["options"][int(user_input) - 1]
                break
            else:
                print("Invalid input. Please enter a valid choice")
                
        if user_choice == q['answer']:
            print("Correct answer")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
                
        print(f"\nYou got {score}/{len(quiz_question)} questions correctly!")
        

if __name__ == "__main__":
    quiz_app()