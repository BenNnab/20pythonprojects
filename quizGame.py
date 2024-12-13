# Python Quiz Game

questions = (
    "1. How many elements are there in the periodic table?: ",
    "2. Which animal lays the largest eggs?: ",
    "3. What is the most abundant gas in Earth's atmosphere?: ",
    "4. How many bones are in the human body?: ",
    "5. Which planet in the solar system is the hotest?: ")

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. oxygen", "C. Carbon_Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
    )
answers = (
    "C",
    "D",
    "A",
    "A",
    "B")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT") 
        print(f"{answers[questions_num]} is the correct answer")
    questions_num += 1
    
print("---------------------------")

print("*********RESULTS***********")

print("---------------------------")

print("Correct Options: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Chosen Options: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f"Your score is: {score}%")