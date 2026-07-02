import requests
import html

# 1. Ask the internet database for 10 math questions
api_url = "https://opentdb.com/api.php?amount=10&category=19"
response = requests.get(api_url)
data = response.json()
questions = data['results']

# Create a variable to keep track of your score
score = 0

# 2. Loop through each of the 10 questions one by one
for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {html.unescape(question['question'])}")
    
    # 3. Combine the wrong answers and the right answer into one list
    correct_answer = html.unescape(question['correct_answer'])
    options = question['incorrect_answers'] + [question['correct_answer']]
    options = [html.unescape(opt) for opt in options]
    options.sort() # Alphabetically sorts them to randomize the order
    
    # 4. Print the choices out as 1, 2, 3, 4
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
        
    # 5. Wait for the player to type their answer
    user_input = input("Your answer (enter the option number): ")
    
    # --- NEW LOGIC: VALIDATION AND SCORING ---
    try:
        # Convert what you typed into a number
        choice_index = int(user_input) - 1
        
        # Check if the text of the option you chose matches the correct answer
        if options[choice_index] == correct_answer:
            print("✨ Correct! Well done.")
            score += 1
        else:
            print(f"❌ Incorrect. The right answer was: {correct_answer}")
    except (ValueError, IndexError):
        # This triggers if you type a letter instead of a number, or a number like 99
        print(f"⚠️ Invalid input. The right answer was: {correct_answer}")

# Final game summary
print(f"\n🎉 Game Over! Your final score is: {score}/10")