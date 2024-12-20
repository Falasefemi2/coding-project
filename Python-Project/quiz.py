import random
import time

class QuizApp:
    def __init__(self, questions):
        """
        Initialize the quiz application with a list of questions.
        
        :param questions: List of dictionaries containing quiz questions
        """
        self.questions = questions
        self.total_questions = len(questions)
        self.score = 0
        self.incorrect_questions = []

    def display_welcome_message(self):
        """Display a welcome message to the user."""
        print("=" * 50)
        print("Welcome to the Comprehensive Quiz Challenge!")
        print("=" * 50)
        print(f"This quiz contains {self.total_questions} questions.")
        print("Test your knowledge and see how well you do!")
        print("=" * 50)
        time.sleep(2)

    def run_quiz(self):
        """
        Run the entire quiz, shuffling questions and tracking performance.
        """
        # Shuffle questions to randomize order
        random.shuffle(self.questions)
        
        self.display_welcome_message()

        for i, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}/{self.total_questions}: {q['question']}")
            
            # Shuffle options to prevent predictability
            options = q['options'].copy()
            random.shuffle(options)
            
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")
            
            user_choice = self.get_valid_input(len(options))
            selected_answer = options[user_choice - 1]
            
            self.evaluate_answer(q, selected_answer)
            
            # Small pause between questions
            time.sleep(1)

        self.display_results()

    def get_valid_input(self, max_options):
        """
        Get a valid input from the user.
        
        :param max_options: Maximum number of options
        :return: Valid user input as an integer
        """
        while True:
            try:
                user_input = int(input("Enter your choice (number): ").strip())
                if 1 <= user_input <= max_options:
                    return user_input
                else:
                    print(f"Please enter a number between 1 and {max_options}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def evaluate_answer(self, question, selected_answer):
        """
        Evaluate the user's answer and update score.
        
        :param question: Current question dictionary
        :param selected_answer: User's selected answer
        """
        if selected_answer == question['answer']:
            print("✅ Correct answer!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {question['answer']}")
            self.incorrect_questions.append(question['question'])

    def display_results(self):
        """Display quiz results with performance analysis."""
        print("\n" + "=" * 50)
        print("Quiz Completed!")
        print(f"Your Score: {self.score}/{self.total_questions}")
        
        # Calculate percentage
        percentage = (self.score / self.total_questions) * 100
        
        # Performance categories
        if percentage == 100:
            print("🏆 Perfect Score! Exceptional Knowledge!")
        elif percentage >= 80:
            print("👏 Excellent Performance!")
        elif percentage >= 60:
            print("👍 Good Job! Room for Improvement.")
        else:
            print("📚 Keep Studying!")
        
        # Show incorrect questions if any
        if self.incorrect_questions:
            print("\nQuestions You Got Wrong:")
            for q in self.incorrect_questions:
                print(f"• {q}")

def main():
    # Expanded and diverse quiz questions
    quiz_questions = [
        # Geography Questions
        {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kaduna"], "answer": "Abuja"},
        {"question": "Which African country is known as the 'Rainbow Nation'?", "options": ["Kenya", "South Africa", "Nigeria"], "answer": "South Africa"},
        {"question": "What is the largest country in Africa by land area?", "options": ["Egypt", "Algeria", "Sudan"], "answer": "Algeria"},
        
        # Political Questions
        {"question": "Who won Nigeria's 2023 presidential election?", "options": ["Peter Obi", "Atiku Abubakar", "Bola Tinubu"], "answer": "Bola Tinubu"},
        {"question": "Which country is Nelson Mandela from?", "options": ["Kenya", "South Africa", "Nigeria"], "answer": "South Africa"},
        
        # Sports Questions
        {"question": "Which team won the English Premier League 4x in a row?", "options": ["Manchester City", "Arsenal", "Liverpool"], "answer": "Manchester City"},
        {"question": "Who won the African Cup of Nations in 2023?", "options": ["Senegal", "Morocco", "Nigeria"], "answer": "Nigeria"},
        {"question": "In what year did Nigeria first win the Olympic football gold?", "options": ["1996", "2000", "1988"], "answer": "1996"},
        
        # Music Questions
        {"question": "Who sang 'Not Like Us'?", "options": ["Kendrick Lamar", "Drake", "J. Cole"], "answer": "Kendrick Lamar"},
        {"question": "Which Nigerian artist won a Grammy in 2024?", "options": ["Burna Boy", "Wizkid", "Davido"], "answer": "Burna Boy"},
        
        # Technology Questions
        {"question": "Which company created ChatGPT?", "options": ["Google", "Microsoft", "OpenAI"], "answer": "OpenAI"},
        {"question": "What does AI stand for?", "options": ["Advanced Intelligence", "Artificial Intelligence", "Automated Interaction"], "answer": "Artificial Intelligence"},
        
        # Entertainment Questions
        {"question": "Who played Black Panther in the Marvel movies?", "options": ["Michael B. Jordan", "Chadwick Boseman", "Daniel Kaluuya"], "answer": "Chadwick Boseman"},
        {"question": "Which Nigerian actor starred in 'Black Panther'?", "options": ["John Boyega", "Chiwetel Ejiofor", "Dayo Okeniyi"], "answer": "Chiwetel Ejiofor"},
        
        # Science Questions
        {"question": "What is the largest planet in our solar system?", "options": ["Saturn", "Earth", "Jupiter"], "answer": "Jupiter"},
        {"question": "Who developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking"], "answer": "Albert Einstein"},
        
        # Historical Questions
        {"question": "In what year did Nigeria gain independence?", "options": ["1960", "1963", "1965"], "answer": "1960"},
        {"question": "Who was Nigeria's first president?", "options": ["Nnamdi Azikiwe", "Obafemi Awolowo", "Abubakar Tafawa Balewa"], "answer": "Nnamdi Azikiwe"},
        
        # Random Knowledge
        {"question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa"], "answer": "Ottawa"},
        {"question": "Which is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino"], "answer": "Vatican City"}
    ]

    # Create and run quiz
    quiz = QuizApp(quiz_questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()

